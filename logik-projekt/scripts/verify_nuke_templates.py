
import os
import sys

# Add project root and logik-projekt to sys.path
# This script is located in logik-projekt/scripts/
logik_projekt_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if logik_projekt_root not in sys.path:
    sys.path.insert(0, logik_projekt_root)

# Also add the parent directory to allow "logik-projekt.src..." if needed
project_root = os.path.dirname(logik_projekt_root)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.core.functions.io.render_template import render_template

def verify():
    print("Verifying Nuke Template Rendering (string.Template)...")
    
    templates_dir = os.path.join(project_root, 'logik-projekt', 'cfg', 'templates', 'foundry', 'nuke')
    shot_template = os.path.join(templates_dir, 'nuke_shot_script.nk.template')
    read_template = os.path.join(templates_dir, 'nuke_read_node.nk.template')
    
    shot_context = {
        'SHOT_NAME': 'test_shot',
        'APP_NAME': 'nuke',
        'TASK_TYPE': 'comp',
        'VERSION_NAME': 'v001',
        'SHOT_RENDERS_DIR': '/tmp/renders',
        'NUKE_START_FRAME': 'NUKE_START_FRAME',
        'NUKE_END_FRAME': 'NUKE_END_FRAME'
    }
    
    rendered_shot = render_template(shot_template, shot_context)
    print("\nRendered Shot Script Snippet:")
    print(rendered_shot[:250])
    
    assert 'test_shot_nuke_comp_v001.nk' in rendered_shot
    # string.Template safe_substitute will leave ${NUKE_START_FRAME} if it's NOT in context
    # But now we DO pass it in create_nuke_shot_script.
    # In this test, we are testing the TEMPLATE rendering directly.
    assert 'NUKE_START_FRAME' in rendered_shot
    
    read_context = {
        'SHOT_SOURCE_VERSION_SEQUENCE_DIR': '/tmp/source',
        'SHOT_SOURCE_VERSION_START_FRAME': 1001,
        'SHOT_SOURCE_VERSION_END_FRAME': 1100,
        'SHOT_SOURCE_DIR': 'source_A',
        'TASK_TYPE': 'comp',
        'VERSION_NAME': 'v001'
    }
    
    rendered_read = render_template(read_template, read_context)
    print("\nRendered Read Node Snippet:")
    print(rendered_read)
    
    assert 'file "/tmp/source"' in rendered_read
    assert 'first 1001' in rendered_read
    assert 'name "source_A_comp_v001"' in rendered_read
    
    print("\nVerification SUCCESSFUL!")

if __name__ == "__main__":
    verify()
