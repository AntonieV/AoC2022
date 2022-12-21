 
# https://adventofcode.com/2022/day/1
# AoC 2022 - 1_1

input_data = "aoc2022_data/aoc2022_1.txt"

cal_max = 0
elf_max = 0
    
with open(input_data, 'r') as f_in:
    lines = f_in.read()
    elves=lines.split('\n\n')
    num_elves = len(elves)
    for idx, elf in enumerate(elves):
        elf = elf.split('\n')
        items = [int(item) for item in elf if item != '']        
        cal_sum = sum(items)
        if cal_sum > cal_max:
            cal_max = cal_sum
            elf_max = idx
print(f"Elf {elf_max} carrying {cal_max} calories.")
