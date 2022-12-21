# https://adventofcode.com/2022/day/10
# AoC 2022 - 10_1


def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]


input_data = "aoc2022_data/aoc2022_10.txt"
lines = get_input_data(input_data)

register_vals = [1]
cycles2read = [20, 60, 100, 140, 180, 220]

for line in lines:
    line = line.split()
    register_vals.append(register_vals[-1])
    if len(line) > 1:
        register_vals.append(register_vals[-1] + int(line[1]))

total_signal = sum([register_vals[i - 1] * i for i in cycles2read])
print("The sum of the signal strengths during the 20th, 60th, 100th, 140th, 180th, and 220th " \
      f"cycles is: {total_signal}") 
