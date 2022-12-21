 
# https://adventofcode.com/2022/day/3
# AoC 2022 - 3_1

import string

input_data = "aoc2022_data/aoc2022_3.txt"

alphabet_low = list(string.ascii_lowercase)
alphabet_up = list(string.ascii_uppercase)
priorities = list(range(1,53))
ranks = dict(zip(alphabet_low + alphabet_up, priorities))

sum_priorities = 0

with open(input_data, 'r') as f_in:
    lines = f_in.readlines()
    for line in lines: 
        line = line.strip('\n')
        if not len(line) % 2 == 0:
            print("There are an odd number of items in rucksack!")
        mid_line = int(len(line)/2)
        first_compartment = list(line[:mid_line])
        second_compartment = list(line[mid_line:])
        duplicates = []
        for item in first_compartment:
            if item in second_compartment:
                duplicates.append(ranks[item])
        sum_priorities += sum(set(duplicates))
print(f"The sum of duplicate items rank is {sum_priorities}.")
