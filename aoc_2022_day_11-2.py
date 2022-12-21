 
# AoC 2022 - 11_2
import re
import numpy as np
import math

class Monkey:
    def __init__(self, name):
        self.monkey_id = name
        self.items = []
        self.operation = ['+', 0]
        self.divisible = 1
        self.next_monkey = [-1, -1]
        self.inspection_count = 0
  
    def get_values(self, text: str, merge=True):
        return int(''.join(re.findall(r'\b\d+\b', text))) if merge else \
            [int(item) for item in re.findall(r'\b\d+\b', text)]
        
    def parse_monkey(self, _line):
        attr, properties = _line.split(': ')
        if attr == 'Starting items':
            self.items = self.get_values(properties, False)
        if attr == 'Operation':
            if properties.endswith('old'):
                self.operation[0] = '**'
                self.operation[1] = 2
            else:
                self.operation[0] = ''.join([op for op in ['*', '/', '+', '-' ] if op in properties])
                self.operation[1] = self.get_values(properties)
        if attr == 'Test':
            self.divisible = self.get_values(properties)
        if attr == 'If true':
            self.next_monkey[0] = self.get_values(properties)
        if attr == 'If false':
            self.next_monkey[1] = self.get_values(properties)


        
def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]


def monkeys_play(_monkeys: dict, _rounds: int):    
    # see https://de.wikipedia.org/wiki/Prime_Restklassengruppe
    prim_factor = np.prod([monkey.divisible for _id, monkey in _monkeys.items()])
    for _round in range(1, _rounds + 1):
        init_op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '**': lambda x, y: x ** y
        }
        for _id, monkey in _monkeys.items():
            items = monkey.items
            if items:
                for item in items:
                    monkey.inspection_count += 1
                    op = monkey.operation
                    item = init_op[op[0]](item, op[1])
                    idx = 0 if item % monkey.divisible == 0 else 1
                    next_monkey = _monkeys[str(monkey.next_monkey[idx])]
                    next_monkey.items.append(item % prim_factor)
                monkey.items = []

                
input_data = "aoc2022_data/aoc2022_11.txt"
lines = get_input_data(input_data)

num_rounds = 10000
number_most_active = 2
monkeys = dict()

for line in lines:
    if line:
        if line.endswith(':'):
            monkey_name = ''.join(re.findall(r'\b\d+\b', line))
            monkey = Monkey(monkey_name)
        else:
            monkey.parse_monkey(line)
            if 'If false: throw to monkey' in line:
                monkeys[str(monkey.monkey_id)] = monkey

monkeys_play(monkeys, num_rounds)

inspections = []

for monkey in monkeys:
    inspections.append(monkeys[monkey].inspection_count)
    print(f"Monkey {monkeys[monkey].monkey_id}: inpected {monkeys[monkey].inspection_count} times.")

monkey_business = np.prod(sorted(inspections, reverse=True)[:number_most_active])

print(f"Level of monkey business after {num_rounds} rounds is for the {number_most_active} " \
      f"most active monkeys: {monkey_business}.")
