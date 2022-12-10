# DAY08
def parse_row(line):
    return [int(s) for s in line]


def compute_visible_dir(rows, visible, start, direction):
    w, h = len(rows[0]), len(rows)
    x, y = start
    dx, dy = direction
    maxh = -1
    while x >= 0 and x < w and y >= 0 and y < h:
        ch = rows[y][x]
        if ch > maxh:
            maxh = ch
            visible[y][x] += 1
        x += dx
        y += dy


def compute_visible(rows):
    w = len(rows[0])
    h = len(rows)
    res = [[0] * w for _ in range(h)]

    for j in range(h):
        compute_visible_dir(rows, res, (0, j), (1, 0))
        compute_visible_dir(rows, res, (w - 1, j), (-1, 0))
    for i in range(w):
        compute_visible_dir(rows, res, (i, 0), (0, 1))
        compute_visible_dir(rows, res, (i, h - 1), (0, -1))
    return res


def get_score_dir(rows, pos, direction):
    w, h = len(rows[0]), len(rows)
    x, y = pos
    maxh = rows[y][x]
    dx, dy = direction
    x += dx
    y += dy
    res = 0
    while x >= 0 and x < w and y >= 0 and y < h:
        ch = rows[y][x]
        res += 1
        if ch >= maxh:
            return res
        x += dx
        y += dy
    return res


def get_score(rows, pos):
    w, h = len(rows[0]), len(rows)
    res = 1
    res *= get_score_dir(rows, pos, (1, 0))
    res *= get_score_dir(rows, pos, (0, 1))
    res *= get_score_dir(rows, pos, (-1, 0))
    res *= get_score_dir(rows, pos, (0, -1))
    return res


def solution():
    rows = [parse_row(s.strip()) for s in open("../data/08.txt").readlines()]
    w, h = len(rows[0]), len(rows)

    visible = compute_visible(rows)
    res1 = sum(sum(c > 0 for c in row) for row in visible)

    res2 = max(max(get_score(rows, (x, y)) for y in range(h)) for x in range(w))
    print(f"Answer 1: {res1}\nAnswer 2: {res2}")
