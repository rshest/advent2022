def halve(s):
    n = int(len(s) / 2)
    return [s[:n], s[n:]]


def get_priority(c):
    n = ord(c)
    if n >= ord('a') and n <= ord('z'):
        return n - ord('a') + 1
    elif n >= ord('A') and n <= ord('Z'):
        return n - ord('A') + 27
    else:
        return 0


def get_matching(a, b):
    return set(a).intersection(set(b))


def solution():
    lines = [s.strip() for s in open("../data/03.txt").readlines()]
    halves = [halve(s) for s in lines]
    matching = [get_matching(x, y) for x, y in halves]
    res1 = sum(sum(get_priority(x) for x in s) for s in matching)

    res2 = 0
    for i in range(0, len(lines), 3):
        matches = set(lines[i]).intersection(
            set(lines[i + 1])).intersection(set(lines[i + 2]))
        res2 += sum(get_priority(x) for x in matches)

    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
