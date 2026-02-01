import numpy as np
from pathlib import Path
from typing import Union

def convert_splat_to_standard_ply(input_ply: Union[str, Path], output_ply: Union[str, Path]) -> bool:
    """
    Converts a 3D Gaussian Splat PLY (which often contains SH parameters and scales)
    into a standard XYZ RGB point cloud PLY that Flame's Action node can import.
    """
    input_path = Path(input_ply)
    output_path = Path(output_ply)

    if not input_path.exists():
        return False

    # Note: Gaussian Splat PLYs are usually binary and have complex headers.
    # We use 'plyfile' library for robust implementation.
    try:
        from plyfile import PlyData, PlyElement
    except ImportError:
        # Dependency check: plyfile is required for this conversion.
        return False

    try:
        plydata = PlyData.read(input_path)
        vertex = plydata['vertex']
        
        # Extract basic geometry (always present in 3DGS)
        x = vertex['x']
        y = vertex['y']
        z = vertex['z']
        
        # Extract base color (f_dc_0, 1, 2 in 3DGS format)
        # 3DGS stores these as Spherical Harmonics (SH) coefficients. 
        # The f_dc terms represent the DC (zero-order) component.
        # Conversion to RGB requires applying the SH constant C0.
        SH_C0 = 0.28209479177387814
        
        # Calculate RGB from DC coefficients
        # Formula: 0.5 + SH_C0 * dc_coeff
        r = (0.5 + SH_C0 * vertex['f_dc_0']) * 255
        g = (0.5 + SH_C0 * vertex['f_dc_1']) * 255
        b = (0.5 + SH_C0 * vertex['f_dc_2']) * 255
        
        # Clip to valid 8-bit color range
        r = np.clip(r, 0, 255).astype(np.uint8)
        g = np.clip(g, 0, 255).astype(np.uint8)
        b = np.clip(b, 0, 255).astype(np.uint8)

        # Structure data for standard XYZ RGB PLY
        vertex_data = np.empty(len(x), dtype=[
            ('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
            ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')
        ])
        vertex_data['x'] = x
        vertex_data['y'] = y
        vertex_data['z'] = z
        vertex_data['red'] = r
        vertex_data['green'] = g
        vertex_data['blue'] = b

        # Write out as standard PLY (text-based for maximum compatibility with Flame)
        el = PlyElement.describe(vertex_data, 'vertex')
        PlyData([el], text=True).write(output_path)
        
        return True
    except Exception as e:
        # Errors usually stem from incompatible PLY schemas or missing properties.
        return False
