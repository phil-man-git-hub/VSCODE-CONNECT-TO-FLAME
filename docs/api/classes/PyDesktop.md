# Class: PyDesktop

**Module**: `flame`

Class derived from PyArchiveEntry. This class represents a Desktop.

## Methods
### `children(...)`

None( (flame.PyDesktop)arg1) -> list

### `batch_groups(...)`

None( (flame.PyDesktop)arg1) -> list

### `reel_groups(...)`

None( (flame.PyDesktop)arg1) -> list

### `create_reel_group(...)`

create_reel_group( (PyDesktop)arg1, (str)name) -> object :
    Create a new Reel Group object in the Desktop catalogue.

### `save(...)`

save( (PyDesktop)arg1) -> bool :
    Save the Desktop to the location defined by the *destination* attribute.

### `create_batch_group(...)`

create_batch_group( (PyDesktop)arg1, (str)name [, (object)nb_reels=None [, (object)nb_shelf_reels=None [, (list)reels=[] [, (list)shelf_reels=[] [, (int)start_frame=1 [, (object)duration=None]]]]]]) -> object :
    Create a new Batch Group object in the Desktop catalogue.
    Keyword arguments:
    name -- Name of the Batch Group.
    nb_reels -- Number of reels created. *reels* overrides *nb_reels*.
    nb_shelf_reels -- Number of shelf reels. The first shelf reel created is named Batch Renders. *shelf_reels* ovverides *nb_shelf_reels*.
    reels -- A list of reel names. Overrides *nb_reels*.
    shelf_reels -- A list of shelf reel names. Overrides *nb_shelf_reels*.
    start_frame -- The Batch Group's start frame. No timecodes, only a frame value.
    duration -- The number of frames. Sets the Duration field in the Batch UI. Will be set to the first clip duration when not specified.

### `clear(...)`

clear( (PyDesktop)arg1) -> bool :
    Clear the Desktop.

