from collections import defaultdict


def get_unique_substring_pos(stream, n):
    counts = defaultdict(lambda: 0)
    for i, c in enumerate(stream):
        counts[c] += 1
        if i >= n:
            cprev = stream[i - n]
            cnt = counts[cprev] - 1
            if cnt == 0:
                del counts[cprev]
            else:
                counts[cprev] = cnt
        if len(counts) == n:
            return i + 1
    return len(stream)


def solution():
    stream = open("../data/06.txt").read()

    res1 = get_unique_substring_pos(stream, 4)
    res2 = get_unique_substring_pos(stream, 14)
    print(f"Answer 1: {res1}\nAnswer 2: {res2}")
