# https://adventofcode.com/2022/day/9
# AoC 2022 - 9_1

import numpy as np

def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]
    

def update_tail(tail_idx: int, head_idx: int):
    # row: head moves right, col: head moves down
    if tail_idx < head_idx:
        return 1
    # row: head moves left, col: head moves up
    if tail_idx > head_idx:
        return -1
    return 0

def get_save_matrix_size(_lines: list):
    max_rows, max_cols = 1, 1
    sum_up, sum_right = 0, 0
    for line in _lines: 
        direction, steps = line.split()
        steps = int(steps)
        if direction == 'U' or direction == 'D':        
            max_rows += steps
            sum_up += steps if direction == 'U' else 0
        if direction == 'R' or direction == 'L':
            max_cols += steps
            sum_right += steps if direction == 'R' else 0
    _grid = np.zeros((max_rows, max_cols))
    _start = {'row': sum_up, 'col': sum_right}        
    return _grid, {'row': sum_up, 'col': sum_right}, {'row': sum_up, 'col': sum_right}



input_data = "aoc2022_data/aoc2022_9.txt"
lines = get_input_data(input_data)


# get maximum matrix size: sum all up and down for vertical (= rows) and 
# all right and left values for horizontal (= cols) direction
# one additional row and col for start position

grid, t_pos, h_pos = get_save_matrix_size(lines)
grid[h_pos['row'], h_pos['col']] = 1

for line in lines:
    direction, steps = line.split()
    steps = int(steps)
    for step in range(steps):
        
        # move head    
        if direction == 'U':
            h_pos['row'] -= 1
        if direction == 'D':
            h_pos['row'] += 1
        if direction == 'L':
            h_pos['col'] -= 1
        if direction == 'R':
            h_pos['col'] += 1
            
        # update tail  
        # critical diagnoal distance  
        if abs(t_pos['row'] - h_pos['row']) + abs(t_pos['col'] - h_pos['col']) > 2: 
            t_pos['row'] += update_tail(t_pos['row'], h_pos['row'])
            t_pos['col'] += update_tail(t_pos['col'], h_pos['col'])
        # critical horizontal distance         
        elif abs(t_pos['row'] - h_pos['row']) > 1 and abs(t_pos['col'] - h_pos['col']) <= 1:
            t_pos['row'] += update_tail(t_pos['row'], h_pos['row'])
        # critical vertical distance
        elif abs(t_pos['row'] - h_pos['row']) <= 1 and abs(t_pos['col'] - h_pos['col']) > 1: 
            t_pos['col'] += update_tail(t_pos['col'], h_pos['col'])
            
        # mark as visited
        grid[t_pos['row'], t_pos['col']] = 1

t_visited = int(grid.sum())
print(f"{t_visited} positions are visited by the tail of the rope at least once.") 
