#

# -------------------------------------------------------------------------- #

# File Name:        pathfinder_abs.py
# Version:          0.4.5
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import os
import sys

# ========================================================================== #
# This section locates the running script and absolute paths.
# ========================================================================== #

class abs_path_info:
    def __init__(self, script_name):
        """
        Initializes the abs_path_info object using lp_bootstrap for path resolution.
        """
        import lp_bootstrap
        
        paths = lp_bootstrap.paths
        
        self.script_name = script_name
        self.abs_path_to_this_script = os.path.dirname(os.path.abspath(script_name))
        self.abs_script_dir = os.path.dirname(script_name)
        self.abs_parent_dir = str(paths["root"])
        
        # Use canonical paths from bootstrap
        self.abs_config_dir = str(paths["cfg"])
        self.abs_scripts_dir = str(paths["src"]) # Mapping 'scripts' to 'src' based on usage
        
        # Construct internal paths based on canonical src
        self.abs_modules_dir = os.path.join(self.abs_scripts_dir, "core")
        self.abs_classes_dir = os.path.join(self.abs_modules_dir, "classes")
        self.abs_functions_dir = os.path.join(self.abs_modules_dir, "functions")
        self.abs_version_dir = str(paths["root"] / "version")


    # ---------------------------------------------------------------------- #

    def create_directories(self):
        """
        Creates necessary directories if they do not exist.
        """

        print("Creating necessary directories...")
        os.makedirs(
            self.abs_modules_dir,
            exist_ok=True
        )

        os.makedirs(
            self.abs_classes_dir,
            exist_ok=True
        )

        os.makedirs(
            self.abs_functions_dir,
            exist_ok=True
        )

    # ---------------------------------------------------------------------- #

    def print_absolute_paths(self):
        """
        Prints out the paths of the running script and related directories.
        """

        print("This script:        ",
              os.path.basename(self.script_name)
        )

        print("Path to this script:",
              os.path.basename(self.abs_path_to_this_script)
        )
        print("Script directory:   ",
              os.path.basename(self.abs_script_dir)
        )
        print("Parent directory:   ",
              os.path.basename(self.abs_parent_dir)
        )
        print("Config directory:   ",
              os.path.basename(self.abs_config_dir)
        )
        print("Scripts directory:  ",
              os.path.basename(self.abs_scripts_dir)
        )
        print("Classes directory:  ",
              os.path.basename(self.abs_classes_dir)
        )
        print("Functions directory:",
              os.path.basename(self.abs_functions_dir)
        )
        print("Version directory:  ",
              os.path.basename(self.abs_version_dir)
        )

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Example usage:
if __name__ == "__main__":
    # Pass the calling script's __file__ attribute
    abs_script_directories = abs_path_info(sys.argv[0])
    abs_script_directories.create_directories()
    abs_script_directories.print_paths()

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# -------------------------------------------------------------------------- #

# Disclaimer:       This program is part of LOGIK-PROJEKT.
#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.

#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.

# -------------------------------------------------------------------------- #
# Changelist:

# -------------------------------------------------------------------------- #
# version:               0.0.5
# modified:              2024-05-12 - 15:37:50
# comments:              Added function to read directories from JSON files.
# -------------------------------------------------------------------------- #
# version:               0.0.6
# modified:              2024-05-12 - 18:16:05
# comments:              Added a 'separators' function and tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.0.7
# modified:              2024-05-14 - 16:30:58
# comments:              Minor reformatting.
# -------------------------------------------------------------------------- #
# version:               0.0.8
# modified:              2024-05-14 - 16:31:23
# comments:              Changed object_colors from python to JSON.
# -------------------------------------------------------------------------- #
# version:               0.0.9
# modified:              2024-05-14 - 16:31:47
# comments:              Tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.1.0
# modified:              2024-05-14 - 16:46:55
# comments:              Production tested in flame 2025.
# -------------------------------------------------------------------------- #
# version:               0.2.0
# modified:              2024-05-14 - 18:05:26
# comments:              Prepped for obsolete code removal. Tested in flame 2025
# -------------------------------------------------------------------------- #
# version:               0.3.0
# modified:              2024-05-14 - 19:27:33
# comments:              Restored 'object_colors' from python function.
# -------------------------------------------------------------------------- #
# version:               0.3.1
# modified:              2024-05-15 - 07:55:47
# comments:              Renamed 'classes_and_functions' dir to 'modules'.
# -------------------------------------------------------------------------- #
# version:               0.4.1
# modified:              2024-05-18 - 18:01:29
# comments:              Added GNU GPLv3 Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.2
# modified:              2024-05-18 - 18:46:51
# comments:              Minor modification to Disclaimer.
# -------------------------------------------------------------------------- #
# version:               0.4.3
# modified:              2024-06-03 - 10:32:22
# comments:              Moved import flame statement to each function
# -------------------------------------------------------------------------- #
# version:               0.4.4
# modified:              2024-06-12 - 12:21:22
# comments:              Restored import flame statement to top of script.
# -------------------------------------------------------------------------- #
# version:               0.4.5
# modified:              2024-08-31 - 18:40:12
# comments:              prep for release.
# -------------------------------------------------------------------------- #
