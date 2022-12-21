# AoC 2022 - 6_2

def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]

input_data = "aoc2022_data/aoc2022_6.txt"
lines = get_input_data(input_data)
current_items = []

for idx, char in enumerate(list(*lines)):
    if len(current_items) < 14:
        if char in current_items:
            idx_shift = current_items.index(char) + 1
            current_items = current_items[idx_shift:]
        current_items.append(char)
    if len(current_items) == 14:
        print(f"The first start-of-message marker is detected after {idx + 1} characters were proceeded, " \
              f"the marker is: {''.join(current_items)}.")
        break 
