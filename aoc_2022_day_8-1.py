 
# https://adventofcode.com/2022/day/8
# AoC 2022 - 8_1

import numpy as np

def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]


input_data = "aoc2022_data/aoc2022_8.txt"
lines = get_input_data(input_data)

forrest = np.array([[*line] for line in lines])
num_cols = len(forrest[:, 0])
num_rows = len(forrest[0, :])
range_col, range_row = (1, num_cols - 1), (1, num_rows - 1)

# all tree at edges are visible, add them to visible_trees
visible_trees = 2 * num_rows + 2 * (num_cols - 2)

for col in range(range_col[0], range_col[1]):
    for row in range(range_row[0], range_row[1]):
        tree = forrest[row, col]
        top = max(forrest[:row, col])
        bottom = max(forrest[row + 1:, col])
        left = max(forrest[row, :col])
        right = max(forrest[row, col + 1:])
        is_visible = min([top, bottom, left, right]) < tree
        if is_visible:
            visible_trees += 1

print(f"{visible_trees} trees are visible from outside the grid.")
