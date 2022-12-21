 
# AoC 2022 - 1_2

input_data = "aoc2022_data/aoc2022_1.txt"

cal_max = []
    
with open(input_data, 'r') as f_in:
    lines = f_in.read()
    elves=lines.split('\n\n')
    num_elves = len(elves)
    for idx, elf in enumerate(elves):
        elf = elf.split('\n')
        items = [int(item) for item in elf if item != '']        
        cal_sum = sum(items)
        if len(cal_max) < 3:
            cal_max.append(cal_sum)
            cal_max = sorted(cal_max)
        else:
            if cal_sum > cal_max[0]:
                cal_max = [cal_sum] + cal_max[1:]
                cal_max = sorted(cal_max)
print(f"The top three elves carrying {sum(cal_max)} calories.")
