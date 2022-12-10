# DAY07
import sys

class Node:
    def __init__(self, is_directory=True, size=0):
        self.children = {}
        self.is_directory = is_directory
        self.size = size
        self.parent = None
        self.name = ""

    def compute_size(self):
        size = self.size
        if self.is_directory:
            size = sum(ch.compute_size() for ch in self.children.values())
        self.size = size
        return size

def process_commands(lines):
    root = Node()
    root.name = "/"
    cur_node = root

    for line in lines:
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                name = parts[2]
                if name == "..":
                    cur_node = cur_node.parent
                elif name == "/":
                    cur_node = root
                else:
                    cur_node = cur_node.children[name]
        else:
            is_directory = parts[0] == "dir"
            child = Node(is_directory)
            name = parts[1]
            child.name = name
            child.parent = cur_node
            if not is_directory:
                child.size = int(parts[0])
            cur_node.children[name] = child
    root.compute_size()
    return root

def get_sum_at_most(node, n):
    if not node.is_directory:
        return 0
    res = 0
    if node.size <= n:
        res += node.size
    return res + sum(get_sum_at_most(ch, n) for ch in node.children.values())

def get_min_to_delete(node, to_free):
    res = sys.maxsize
    if not node.is_directory:
        return res
    if node.size >= to_free:
        res = node.size
    return min(res, min(get_min_to_delete(ch, to_free) for ch in node.children.values()))

def solution():
    lines = [s.strip() for s in open("../data/07.txt").readlines()]

    root = process_commands(lines)
    res1 = get_sum_at_most(root, 100000)
    to_free = 30000000 - (70000000 - root.size)
    res2 = get_min_to_delete(root, to_free)
    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
