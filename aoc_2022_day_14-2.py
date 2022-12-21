 
mischgemüsemischgemüse# AoC 2022 - 14_2

import numpy as np

        
def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]
    
    
def apply_missing_fields(x_list, y_list):
    x_coord, y_coord = [], []
    for i in range(len(x_list) - 1):
        diff_x = x_list[i] - x_list[i + 1]
        diff_x_abs = abs(diff_x)
        
        diff_y = y_list[i] - y_list[i + 1]
        diff_y_abs = abs(diff_y)
        
        x_coord.append(x_list[i])
        y_coord.append(y_list[i])
        
        if diff_x_abs > 1 and diff_y_abs <= 1:
            for j in range(1, diff_x_abs):
                if diff_x > 1:
                    x_coord.append(x_list[i] - j)
                    y_coord.append(y_list[i])                
                if diff_x < -1:
                    x_coord.append(x_list[i] + j)
                    y_coord.append(y_list[i])  
                                   
        if diff_y_abs > 1 and diff_x_abs <= 1:
            for j in range(1, diff_y_abs):
                if diff_y > 1:
                    y_coord.append(y_list[i] - j)
                    x_coord.append(x_list[i])                
                if diff_y < -1:
                    y_coord.append(y_list[i] + j)
                    x_coord.append(x_list[i]) 
    x_coord.append(x_list[-1]) 
    y_coord.append(y_list[-1]) 
    return x_coord, y_coord


def scan_paths(_lines: str, space_to_ground: int):
    max_x, max_y, _paths = 0, 0, []
    for _line in _lines:
        _line = [int(item) for items in _line.split(' -> ') for item in items.split(',')]
        x_path = _line[::2]
        y_path = _line[1::2]
        x_path, y_path = apply_missing_fields(x_path, y_path)
        max_x = max(max_x, max(x_path))        
        max_y = max(max_y, max(y_path))
        _paths.append([y_path, x_path])     
    max_y += space_to_ground + 1
    estimated_x_range = max_x + 2 * max_y
    arr = np.chararray((max_y, max_x + estimated_x_range))
    arr[:] = '.'
    ground = len(arr[-1, :])
    arr[-1,:] = ['#'] * ground        
    return arr, _paths, estimated_x_range // 2 + 1
    

def draw_paths(_scan,_paths: list, left_x):
    for _path in _paths:        
        for row, col in zip(_path[0], _path[1]):
            _scan[row][col + left_x] = '#'

            
def sand_runs(scan, start_col):
    count = 0    
    num_rows = len(scan[:,start_col])
    row = 0
    col = start_col
    while True:
        count_start = count
        bottom_blocked = scan[row + 1][col].decode() != '.'
        left_blocked = scan[row + 1][col - 1].decode() != '.'
        right_blocked = scan[row + 1] [col + 1].decode() != '.'
        
        if bottom_blocked:                    
            if left_blocked and not right_blocked:
                col += 1
            elif left_blocked and right_blocked:
                scan[row][col] = 'o'
                count += 1
                if row == 0:
                    return scan, count  
                row, col = 0, start_col
                continue
            elif not left_blocked:
                col -= 1        
        row += 1
        if row >= num_rows - 1:
            row = 0  
           
        

input_data = "aoc2022_data/aoc2022_14.txt"
out_file = "results/aoc2022_14-2_picture.txt"
lines = get_input_data(input_data)
sand_start_col = 500
space_to_ground = 2


ground_scan, paths, left_x_range = scan_paths(lines, space_to_ground)
sand_start_col += left_x_range
draw_paths(ground_scan, paths, left_x_range)
ground_scan, _count = sand_runs(ground_scan, sand_start_col)

with open(out_file, 'w') as f_out:    
    for line in ground_scan.decode():
        f_out.write(''.join(line) + '\n')

print(f"{_count} units of sand come to rest.")
