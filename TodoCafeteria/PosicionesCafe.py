from copy import deepcopy

movement_steps = [{'vel': 0, 'movement_axis': 'stop', 'number_movements': 10},
                  {'vel': -25, 'movement_axis': 'y', 'number_movements': 30},
                  {'vel': -25, 'movement_axis': 'x', 'number_movements': 4},
                  {'vel': 0, 'movement_axis': 'stop', 'number_movements': 5}]
initial_position = [600, 820]

all_the_way_back = True

entity_pos_mapping_supp = []

current_position = initial_position
for movement_info in movement_steps:
    for n_step in range(movement_info['number_movements']):
        if movement_info['movement_axis'] == 'x':
            current_position[0] += movement_info['vel']
        elif movement_info['movement_axis'] == 'y':
            current_position[1] += movement_info['vel']
        elif movement_info['movement_axis'] == 'stop':
            pass
        entity_pos_mapping_supp.append(deepcopy(current_position))


if all_the_way_back:
    entity_pos_mapping_supp.extend(entity_pos_mapping_supp[1:-1][::-1])

print(entity_pos_mapping_supp)

