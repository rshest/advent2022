import re

def parse(line):
    parts = re.split("-|,", line)
    return [int(p) for p in parts]

def contains(x, y, a, b):
    return x >= a and y <= b

def overlaps(x, y, a, b):
    return (x <= b and y >= a) or (a <= y and b >= x)

def solution():
    data = [parse(s.strip()) for s in open("../data/04.txt").readlines()]
    res1 = sum(contains(s[0], s[1], s[2], s[3]) or
            contains(s[2], s[3], s[0], s[1]) for s in data)
    res2 = sum(overlaps(s[0], s[1], s[2], s[3]) for s in data)

    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
