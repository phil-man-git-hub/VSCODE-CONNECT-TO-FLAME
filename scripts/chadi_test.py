import flame

# 1. Get Desktop
desktop = flame.project.current_project.current_workspace.desktop

# 2. Cleanup existing if necessary
for item in desktop.batch_groups:
    if item.name == 'chadi-test':
        try:
            flame.delete(item)
        except:
            pass

# 3. Create Batch Group
bg = desktop.create_batch_group('chadi-test')
print(f'Created Batch Group: {bg.name}')

# 4. Create Schematic Reels
reels = ['sources', 'precomp', 'comp']
for r_name in reels:
    bg.create_reel(r_name)
    print(f'Created Reel: {r_name}')

# 5. Create Nodes
mux1 = bg.create_node('Mux')
mux2 = bg.create_node('Mux')
tw = bg.create_node('Timewarp')
write_node = bg.create_node('Write File')
write_node.name = 'chadi-test-comp'

# 6. Connect Nodes
# connect_nodes(source_node, socket_name, dest_node, socket_name)
bg.connect_nodes(mux1, 'Result', tw, 'Front')
bg.connect_nodes(mux2, 'Result', tw, 'Matte')
bg.connect_nodes(tw, 'Result', write_node, 'Front')

print('Successfully created Batch group and connected nodes.')
