 
# https://adventofcode.com/2022/day/4
# AoC 2022 - 4_1

import re


def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]
    
    
input_data = "aoc2022_data/aoc2022_4.txt"
lines = get_input_data(input_data)

num_full_intersect = 0

for item in lines:
    items = [int(i) for i in re.split(',|-', item)]
    if (items[0] >= items[2] and items[1] <= items[3]) or (items[0] <= items[2] and items[1] >= items[3]):
        num_full_intersect += 1

print(f"{num_full_intersect} of the assignment pairs overlap fully the other.")
