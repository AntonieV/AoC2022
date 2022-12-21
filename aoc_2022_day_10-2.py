 
# AoC 2022 - 10_2


def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]


def write_crt_cycle(current_crt, sprite_idx, sprite_length):
    if len(current_crt) in range(sprite_idx, sprite_idx + sprite_length):
        return '#'
    return '.'


def check_line_switch(_current_crt, line_length, _crt_all):
    if len(_current_crt) >= line_length:
        _crt_all.append(_current_crt[:line_length])
        _current_crt = _current_crt[line_length:] 
    return _current_crt, _crt_all


input_data = "aoc2022_data/aoc2022_10.txt"
lines = get_input_data(input_data)

sprite_pos = 0
sprite_len = 3
crt_line_lenght = 40
current_crt = ''
crt_all = []

for line in lines:
    line = line.split()        
    current_crt += write_crt_cycle(current_crt, sprite_pos, sprite_len)
    current_crt, crt_all = check_line_switch(current_crt, crt_line_lenght, crt_all)
    if len(line) > 1:      
        current_crt += write_crt_cycle(current_crt, sprite_pos, sprite_len)
        current_crt, crt_all = check_line_switch(current_crt, crt_line_lenght, crt_all)
        sprite_pos += int(line[1])
    

print("This eight capital letters appear:\n")
for item in crt_all:
    print(item)
