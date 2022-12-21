 
# AoC 2022 - 2_2

input_data = "aoc2022_data/aoc2022_2.txt"
opponent = ['A', 'B', 'C']
self_alphabet = ['A', 'B', 'C']
# 'Y' = draw = rot0 -> index 0, 'Z' = win = rot1 -> index 1, 'X' = lose = rot2 -> index 2
rotations = ['Y', 'Z', 'X']
round_outcome = [3, 6, 0]
total_score = 0

with open(input_data, 'r') as f_in:
    lines = f_in.readlines()
    for line in lines: 
        line = line.strip('\n').split(' ')    
        opp_call = opponent.index(line[0])
        rot = rotations.index(line[1])
        res_round = round_outcome[rot]
        select = self_alphabet[(opp_call + rot) % len(self_alphabet)]
        res_shape = self_alphabet.index(select) + 1
        total_score += res_round + res_shape
print(f"Total score: {total_score}.")
