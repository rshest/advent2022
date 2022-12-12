# DAY09
import math


def parse_move(line):
    parts = line.split(" ")
    return (parts[0], int(parts[1]))


def sign(a):
    return (a > 0) - (a < 0)


def get_tail_pos(ph, pt):
    xh, yh = ph
    xt, yt = pt
    dx, dy = xh - xt, yh - yt
    if abs(dx) + abs(dy) >= 3:
        dx = sign(dx) * math.ceil(abs(dx) / 2)
        dy = sign(dy) * math.ceil(abs(dy) / 2)
    else:
        dx = sign(dx) * math.floor(abs(dx) / 2)
        dy = sign(dy) * math.floor(abs(dy) / 2)
    return (xt + dx, yt + dy)


DIRS = {
    'R': (1, 0),
    'U': (0, 1),
    'L': (-1, 0),
    'D': (0, -1),
}


def eval_tail_pos(moves, n):
    pos = [(0, 0) for _ in range(n)]
    tpos = set()
    tpos.add(pos[-1])
    for (d, nm) in moves:
        dx, dy = DIRS[d]
        ex, ey = pos[0][0] + nm * dx, pos[0][1] + nm * dy
        while pos[0][0] != ex or pos[0][1] != ey:
            # move head
            pos[0] = (pos[0][0] + dx, pos[0][1] + dy)
            # move the tails
            for i in range(1, n):
                pos[i] = get_tail_pos(pos[i - 1], pos[i])
            tpos.add(pos[-1])
    return tpos


def solution():
    moves = [parse_move(s) for s in open("../data/09.txt").readlines()]

    res1 = len(eval_tail_pos(moves, 2))
    res2 = len(eval_tail_pos(moves, 10))

    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
