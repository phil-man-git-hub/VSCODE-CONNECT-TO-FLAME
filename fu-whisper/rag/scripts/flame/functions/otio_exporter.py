"""
OTIO Exporter for Autodesk Flame
--------------------------------
Translates a Flame PySequence into an OpenTimelineIO (.otio) file.

Path: fu-whisper/rag/scripts/flame/functions/otio_exporter.py
"""

import flame
import opentimelineio as otio
import os

class FlameOTIOExporter:
    def __init__(self):
        pass

    def _parse_fps(self, fps_str):
        """Converts Flame frame rate string (e.g. '24 fps') to float."""
        try:
            return float(str(fps_str).split()[0])
        except:
            return 24.0

    def _flame_time_to_otio(self, py_time, rate=None):
        """Converts Flame PyTime or int to OTIO RationalTime."""
        if hasattr(py_time, "frame"):
            fps = self._parse_fps(py_time.frame_rate)
            return otio.opentime.RationalTime(float(py_time.frame), fps)
        else:
            # Handle int/float (frame number)
            return otio.opentime.RationalTime(float(py_time), float(rate) if rate else 24.0)

    def _create_marker(self, py_marker):
        """Converts Flame PyMarker to OTIO Marker."""
        start_time = self._flame_time_to_otio(py_marker.location)
        marked_range = otio.opentime.TimeRange(start_time, otio.opentime.RationalTime(1, start_time.rate))
        
        return otio.schema.Marker(
            name=str(py_marker.name),
            marked_range=marked_range,
            comment=str(py_marker.comment)
        )

    def sequence_to_otio(self, sequence):
        """
        Main conversion logic.
        sequence: flame.PySequence
        returns: otio.schema.Timeline
        """
        timeline = otio.schema.Timeline(name=str(sequence.name).strip("'"))
        
        fps = self._parse_fps(sequence.frame_rate)

        # Set global start time
        timeline.global_start_time = self._flame_time_to_otio(sequence.start_frame, rate=fps)
        
        # We process the current version
        current_version = sequence.versions[0]
        
        # 1. Video Tracks
        for f_track in current_version.tracks:
            otio_track = otio.schema.Track(name=str(f_track.parent.name).strip("'"), kind=otio.schema.TrackKind.Video)
            
            for segment in f_track.segments:
                if segment.type == "Gap":
                    gap_duration = self._flame_time_to_otio(segment.record_duration)
                    otio_item = otio.schema.Gap(duration=gap_duration)
                else:
                    # Create Clip
                    source_range = otio.opentime.TimeRange(
                        start_time=self._flame_time_to_otio(segment.source_in),
                        duration=self._flame_time_to_otio(segment.source_duration)
                    )
                    
                    media_ref = otio.schema.ExternalReference(
                        target_url=str(segment.file_path) if segment.file_path else ""
                    )
                    
                    otio_item = otio.schema.Clip(
                        name=str(segment.source_name).strip("'"),
                        media_reference=media_ref,
                        source_range=source_range
                    )
                
                # Add markers to the segment
                for m in segment.markers:
                    otio_item.markers.append(self._create_marker(m))
                
                # Add Timewarp effects
                for effect in segment.effects:
                    if effect.type == "Timewarp":
                        try:
                            speed_pct = 100.0
                            mode = "unknown"
                            
                            # Try Speed mode
                            try:
                                speed_pct = float(effect.get_speed(0.0))
                                mode = "speed"
                            except Exception as e:
                                if "Speed mode" in str(e):
                                    # Fallback to Timing mode
                                    mode = "timing"
                                    # get_timing returns a float representing the source frame
                                    t0 = effect.get_timing(0.0)
                                    t1 = effect.get_timing(1.0)
                                    # Effective speed = (source_delta / record_delta) * 100
                                    speed_pct = (float(t1) - float(t0)) * 100.0
                                else:
                                    raise e

                            time_scalar = speed_pct / 100.0
                            
                            ltw = otio.schema.LinearTimeWarp(
                                name="FlameTimewarp",
                                time_scalar=time_scalar
                            )
                            
                            # Add Flame-specific metadata as per research doc
                            ltw.metadata["flame"] = {
                                "timewarp": {
                                    "schema_version": 1,
                                    "speed": speed_pct,
                                    "input_fps": fps,
                                    "output_fps": fps,
                                    "mode": mode
                                }
                            }
                            otio_item.effects.append(ltw)
                        except Exception as e:
                            print(f"Failed to export Timewarp on {segment.source_name}: {e}")
                    
                otio_track.append(otio_item)
            
            timeline.tracks.append(otio_track)

        # 2. Audio Tracks
        for a_track in sequence.audio_tracks:
             # Flame Audio tracks are handled slightly differently in the API
             # This prototype focuses on Video, but Audio can be added here
             pass

        return timeline

    def export_to_file(self, sequence, output_path):
        """Exports the sequence to the specified OTIO file path."""
        timeline = self.sequence_to_otio(sequence)
        otio.adapters.write_to_file(timeline, output_path)
        return output_path

def export_current_sequence(sequence_name, output_dir="/tmp"):
    """Helper function to find and export a sequence by name."""
    desktop = flame.project.current_project.current_workspace.desktop
    
    # Search for sequence
    target_seq = None
    for rg in desktop.reel_groups:
        for reel in rg.reels:
            for seq in reel.sequences:
                if str(seq.name).strip("'") == sequence_name:
                    target_seq = seq
                    break
    
    if not target_seq:
        raise Exception(f"Sequence '{sequence_name}' not found on desktop.")
        
    exporter = FlameOTIOExporter()
    output_path = os.path.join(output_dir, f"{sequence_name}.otio")
    return exporter.export_to_file(target_seq, output_path)

if __name__ == "__main__":
    # Example usage if run directly in Flame
    try:
        # Assuming we have a sequence called 'edit-001' from previous turns
        path = export_current_sequence("edit-001")
        print(f"EXPORT_SUCCESS: {path}")
    except Exception as e:
        print(f"EXPORT_ERROR: {e}")
