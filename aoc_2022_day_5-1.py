 
# https://adventofcode.com/2022/day/5
# AoC 2022 - 5_1

def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]

input_data = "aoc2022_data/aoc2022_5.txt"
lines = get_input_data(input_data)

crates_levels = []
crates_stacks = {
    '1': 'FTNZMGHJ',
    '2': 'JWV',
    '3': 'HTBJLVG',
    '4': 'LVDCNJPB',
    '5': 'GRPMSWF',
    '6': 'MVNBFCHG',
    '7': 'RMGHD',
    '8': 'DZVMNH',
    '9': 'HFNG'
}
stack_complete = False

for line in lines:
    if line.startswith('move '):
        line = line.split()
        num_move, _from, _to = int(line[1]), str(line[3]), str(line[5])
        to_move = crates_stacks[_from][:num_move]
        crates_stacks[_from] = crates_stacks[_from][num_move:]
        crates_stacks[_to] = to_move[::-1] + crates_stacks[_to]
print(f"Crates at the top of each stack are: {''.join([crates_stacks[str(i)][0] for i in range(1, 10)])}.")
