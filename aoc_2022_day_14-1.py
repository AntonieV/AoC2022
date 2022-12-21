### https://adventofcode.com/2022/day/14
# AoC 2022 - 14_1

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


def scan_paths(_lines: str, _abyss_space: int):
    max_x, max_y, _paths = 0, 0, []
    for _line in _lines:
        _line = [int(item) for items in _line.split(' -> ') for item in items.split(',')]
        x_path = _line[::2]
        y_path = _line[1::2]
        x_path, y_path = apply_missing_fields(x_path, y_path)
        max_x, max_y = max(max_x, max(x_path)), max(max_y, max(y_path))
        _paths.append([y_path, x_path])        
    arr = np.chararray((max_y + abyss_space, max_x + abyss_space))
    arr[:] = '.'
    return arr, _paths
    

def draw_paths(_scan,_paths: list):
    for _path in _paths:        
        for row, col in zip(_path[0], _path[1]):
            _scan[row][col] = '#'

            
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
                row, col = 0, start_col
                continue
            elif not left_blocked:
                col -= 1
                
        row += 1
        if row >= num_rows - 1:
            return scan, count           
           

input_data = "aoc2022_data/aoc2022_14.txt"
lines = get_input_data(input_data)
abyss_space = 10
sand_start_col = 500


ground_scan, paths = scan_paths(lines, abyss_space)
draw_paths(ground_scan, paths)
ground_scan, _count = sand_runs(ground_scan, sand_start_col)

# for line in ground_scan.decode():
#     print(''.join(line))

print(f"{_count} units of sand come to rest before sand starts flowing into the abyss below.")
 
