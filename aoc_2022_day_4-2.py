# AoC 2022 - 4_2

import re


def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]
    
    
input_data = "aoc2022_data/aoc2022_4.txt"
lines = get_input_data(input_data)

num_intersected = 0

for item in lines:
    items = [int(i) for i in re.split(',|-', item)]
    sections_1 = set(section for section in range(items[0], items[1] + 1))
    sections_2 = set(section for section in range(items[2], items[3] + 1))
    if sections_1.intersection(sections_2):
        num_intersected += 1

print(f"In {num_intersected} of the assignment pairs have overlapped ranges.") 
