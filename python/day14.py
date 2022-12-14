# DAY14
def sign(a):
    return (a > 0) - (a < 0)


def parse_line(line):
    points = line.split(" -> ")
    res = []
    for p in points:
        parts = p.split(",")
        res.append((int(parts[0]), int(parts[1])))
    return res


def rasterize(field, line):
    for i in range(1, len(line)):
        x1, y1 = line[i - 1]
        x2, y2 = line[i]
        dx, dy = sign(x2 - x1), sign(y2 - y1)
        while x1 != x2 or y1 != y2:
            field[(x1, y1)] = '#'
            x1 += dx
            y1 += dy
        field[(x1, y1)] = '#'


def pour_sand(field, start, bottom, has_floor=False):
    x, y = start
    if (x, y) in field:
        return False
    while y < bottom + 2:
        y += 1
        if has_floor and y == bottom + 2:
            field[(x, y - 1)] = 'O'
            return True
        if (x, y) not in field:
            continue
        if (x - 1, y) not in field:
            x -= 1
            continue
        if (x + 1, y) not in field:
            x += 1
            continue
        field[(x, y - 1)] = 'O'
        return True
    return False


def num_occupied(field):
    return sum(c == 'O' for c in field.values())


def solution():
    lines = [parse_line(s) for s in open("../data/14.txt").readlines()]
    field = {}
    for line in lines:
        rasterize(field, line)
    bottom = max(y for x, y in field.keys())

    while pour_sand(field, (500, 0), bottom, False):
        pass
    res1 = num_occupied(field)

    while pour_sand(field, (500, 0), bottom, True):
        pass
    res2 = num_occupied(field)

    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
