# AoC 2022 - 9_2

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
    return _grid, sum_up, sum_right



input_data = "aoc2022_data/aoc2022_9.txt"
lines = get_input_data(input_data)
num_knots = 10

# get maximum matrix size: sum all up and down for vertical (= rows) and 
# all right and left values for horizontal (= cols) direction
# one additional row and col for start position

grid, _row, _col = get_save_matrix_size(lines)
snake = dict()
for i in range(num_knots):
    snake[str(i)] = {'row': _row, 'col': _col}
grid[snake['0']['row'], snake['0']['col']] = 1

for line in lines:
    direction, steps = line.split()
    steps = int(steps)
    for step in range(steps):
        for item in snake:
            # move head  
            if item == '0':
                if direction == 'U':
                    snake[item]['row'] -= 1
                if direction == 'D':
                    snake[item]['row'] += 1
                if direction == 'L':
                    snake[item]['col'] -= 1
                if direction == 'R':
                    snake[item]['col'] += 1
            else:
                current = snake[item]
                prev = snake[str(int(item) - 1)]
                # update tail         
                # critical diagnoal distance  
                if abs(current['row'] - prev['row']) + abs(current['col'] - prev['col']) > 2: 
                    current['row'] += update_tail(current['row'], prev['row'])
                    current['col'] += update_tail(current['col'], prev['col'])
                # critical horizontal distance        
                elif abs(current['row'] - prev['row']) > 1 and abs(current['col'] - prev['col']) <= 1:
                    current['row'] += update_tail(current['row'], prev['row'])
                # critical vertical distance
                elif abs(current['row'] - prev['row']) <= 1 and abs(current['col'] - prev['col']) > 1: 
                    current['col'] += update_tail(current['col'], prev['col'])
            
        # mark as visited
        grid[snake[str(num_knots - 1)]['row'], snake[str(num_knots - 1)]['col']] = 1


tail_visited = int(grid.sum())
print(f"{tail_visited} positions are visited by the tail of the rope with {num_knots} knots at least once.") 
