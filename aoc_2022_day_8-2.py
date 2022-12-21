 
# AoC 2022 - 8_2

import numpy as np

def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]

    
def get_direction_score(direction: list, tree: int):
    num_trees = 0
    for neighbor in direction:
        num_trees += 1
        if neighbor >= tree:
            break
    return num_trees

input_data = "aoc2022_data/aoc2022_8.txt"
lines = get_input_data(input_data)

forrest = np.array([[*line] for line in lines])
num_cols = len(forrest[:, 0])
num_rows = len(forrest[0, :])

max_scenic_score = 0

for col in range(num_cols):
    for row in range(num_rows):
        tree = forrest[row, col]
        top = get_direction_score(forrest[:row, col][::-1], tree)
        bottom = get_direction_score(forrest[row + 1:, col], tree)
        left = get_direction_score(forrest[row, :col][::-1], tree)
        right = get_direction_score(forrest[row, col + 1:], tree)
        scenic_score = top * bottom * left * right
        max_scenic_score = max(max_scenic_score, scenic_score)

print(f"{max_scenic_score} is the highest possible scenic score.")
