# Object: import_clips

**Type**: [`function`](../classes/function.md)

## Description


import_clips( (object)path [, (object)destination=None]) -> list :

    Import one or many clips from a path.

    Keyword arguments:

    path -- The path to the media can be:

     - A path to a single media file.

     - A path to a sequence of media files (ie "/dir/clip.[100-2000].dpx").

     - A folder containing media files.

     - A pattern to media files (ie "/dir/{name}_v{version}.{frame}.{extension}").

     - A list of paths.

    destination -- Flame object containing a clip like a reel or a folder object.