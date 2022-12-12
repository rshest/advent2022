# DAY12
import heapq


def find_pos(field, c):
    w, h = len(field[0]), len(field)
    for j in range(h):
        for i in range(w):
            if field[j][i] == c:
                return i, j
    return -1, -1


def get_elevation(c):
    if c == 'E':
        return ord('z')
    if c == 'S':
        return ord('a')
    return ord(c)


def find_shortest_path_len(field, start, end):
    w, h = len(field[0]), len(field)
    candidates = [(0, start)]
    path_lens = {start: 0}
    prev = {start: (-1, -1)}
    while len(candidates) > 0:
        path_len, pos = heapq.heappop(candidates)
        x, y = pos
        if pos == end:
            min_len_for_a = min(path_lens[(i, j)]
                                for i in range(w)
                                for j in range(h)
                                if field[j][i] == 'a' and (i, j) in path_lens)
            return path_lens[pos], min_len_for_a
        c = field[y][x]

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            cx, cy = x + dx, y + dy
            if cx < 0 or cy < 0 or cx >= w or cy >= h:
                continue
            c1 = field[cy][cx]
            cpos = (cx, cy)
            if get_elevation(c) - get_elevation(c1) > 1:
                continue
            cpath_len = path_len + 1
            if cpos not in path_lens or path_lens[cpos] > cpath_len:
                path_lens[cpos] = cpath_len
                prev[cpos] = pos
                heapq.heappush(candidates, (cpath_len, cpos))


def solution():
    field = [s.strip() for s in open("../data/12.txt").readlines()]
    start = find_pos(field, 'S')
    end = find_pos(field, 'E')
    res1, res2 = find_shortest_path_len(field, end, start)
    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
