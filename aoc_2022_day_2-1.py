 
# https://adventofcode.com/2022/day/2
# AoC 2022 - 2_1

input_data = "aoc2022_data/aoc2022_2.txt"
opponent = ['A', 'B', 'C']
# rot0 = draw (rot0 at index = 0 -> idx 0 in round_outcome), 
# rot1 = win (rot1 at index = 1 in round_outcome) , 
# rot2 = loss (rot2 at index = 2 in round_outcome)
self_alphabet = ['X', 'Y', 'Z']
rotations = [0, 1, 2]
round_outcome = [3, 6, 0]
total_score = 0
    
with open(input_data, 'r') as f_in:
    lines = f_in.readlines()
    for line in lines: 
        line = line.strip('\n').split(' ')    
        opp_call = opponent.index(line[0])
        for rot in rotations:
            if line[1] == self_alphabet[(opp_call + rot) % len(self_alphabet)]:
                res_round = round_outcome[rot]
        res_shape = self_alphabet.index(line[1]) + 1
        total_score += res_round + res_shape
print(f"Total score: {total_score}.")
