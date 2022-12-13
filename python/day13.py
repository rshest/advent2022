# DAY13
import json
from functools import cmp_to_key


def parse_signal(s):
    parts = s.split("\n")
    return (json.loads(parts[0]), json.loads(parts[1]))


def sign(a):
    return (a > 0) - (a < 0)


def is_smaller(s1, s2):
    if type(s1) == int and type(s2) == int:
        return sign(s2 - s1)
    if type(s1) == int:
        s1 = [s1]
    if type(s2) == int:
        s2 = [s2]
    n1, n2 = len(s1), len(s2)
    n = min(n1, n2)
    for i in range(n):
        s = is_smaller(s1[i], s2[i])
        if s != 0:
            return s
    return sign(n2 - n1)


def solution():
    signals = ops = [parse_signal(s) for s in open(
        "../data/13.txt").read().split("\n\n")]
    res1 = sum(i + 1 if is_smaller(s1, s2) == 1 else 0
               for i, (s1, s2) in enumerate(signals))

    packets = [[[2]], [[6]]]
    for s1, s2 in signals:
        packets.append(s1)
        packets.append(s2)

    packets.sort(key=cmp_to_key(is_smaller), reverse=True)
    packets
    n1 = packets.index([[2]]) + 1
    n2 = packets.index([[6]]) + 1
    res2 = n1 * n2
    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
