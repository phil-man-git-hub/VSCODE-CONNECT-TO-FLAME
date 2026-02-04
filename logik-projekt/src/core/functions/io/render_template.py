#
# -------------------------------------------------------------------------- #

# File Name:        render_template.py
# Version:          1.1.0
# Created:          2026-02-03
# Modified:         2026-02-03

# ========================================================================== #
# This section imports the necessary modules.
# ========================================================================== #

import os
from string import Template

def render_template(template_path, context):
    """
    Renders a template file using Python's built-in string.Template with the provided context.

    Parameters:
        template_path (str): The absolute path to the template file.
        context (dict): A dictionary of variables to provide to the template.

    Returns:
        str: The rendered template content.
    """
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found at: {template_path}")

    with open(template_path, 'r') as f:
        template_content = f.read()

    template = Template(template_content)
    
    # Use safe_substitute to avoid KeyError if some placeholders are for later-stage substitution
    # (like NUKE_START_FRAME in the shot script)
    return template.safe_substitute(context)
