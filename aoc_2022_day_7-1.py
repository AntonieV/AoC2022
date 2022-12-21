 
# https://adventofcode.com/2022/day/7
# AoC 2022 - 7_1


class Node:
    def __init__(self, _id, parent):
        self.id = _id
        self.parent = parent
        self.children = []
        self.size_files = 0

def file_size_subtree(nodes: dict, node: Node):
    if not node.children:
        return node.size_files
    for child in node.children:
        node.size_files += file_size_subtree(nodes, nodes[child])
    return node.size_files

def get_input_data(in_file: str):
    with open(in_file, 'r') as f_in:
        return [_line.strip() for _line in f_in.readlines()]
    

input_data = "aoc2022_data/aoc2022_7.txt"
lines = get_input_data(input_data)

cd_cmd = '$ cd '
current_node = Node('/', '')
current_node.size_files = 0
current_node.children = []
all_nodes = {'/': current_node}


for line in lines:
    if line and line[0].isdigit():
        current_node.size_files += int(line.split()[0])
        continue
    if line.startswith('dir '):
        if current_node.id != '/':
            current_node.children.append(current_node.id + "/"  + line.replace('dir ', ''))
        else: 
            current_node.children.append(current_node.id + line.replace('dir ', ''))
        continue
    if line.startswith(cd_cmd):
        dir_name = line.replace(cd_cmd, '')
        if dir_name != '..':
            if dir_name != '/':
                parent = current_node.id
                if parent == '/':
                    current_node = Node(parent + dir_name, parent)
                else: 
                    current_node = Node(parent + "/" + dir_name, parent)
                all_nodes[current_node.id] = current_node             
                continue
        else:
            current_node = all_nodes[current_node.parent]

file_size_subtree(all_nodes, all_nodes['/'])
sum_small_dirs = sum([node.size_files for _, node in all_nodes.items() if node.size_files <= 100000])
print(f"The sum of total sizes of all directories with a total size of at most 100000 is {sum_small_dirs}.")   
