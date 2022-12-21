 
# AoC 2022 - 3_2

import string

input_data = "aoc2022_data/aoc2022_3.txt"

alphabet_low = list(string.ascii_lowercase)
alphabet_up = list(string.ascii_uppercase)
priorities = list(range(1,53))
ranks = dict(zip(alphabet_low + alphabet_up, priorities))

sum_priorities = 0

with open(input_data, 'r') as f_in:
    lines = f_in.readlines()
    groups = []
    for idx in range(0, len(lines), 3):
        groups.append(list(lines[idx:idx + 3]))
    for group in groups:
        duplicates = []
        group = [item.strip('\n') for item in group]
        for item in group[0]:
            if item in group[1] and item in group[2]:
                duplicates.append(ranks[item])
        sum_priorities += sum(set(duplicates))
print(f"The sum of badges items rank is {sum_priorities}.")
