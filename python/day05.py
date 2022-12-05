def parse_crates(lines):
    w = int((len(lines[0]) + 1)/4)
    h = len(lines)
    tops = [0] * w
    crates = []
    for j in range(h):
        line = lines[j]
        cline = [' '] * w
        for i in range(w):
            c = line[1 + i * 4]
            cline[i] = c
            if c == ' ':
                tops[i] += 1
        crates.append(cline)
    crates.reverse()
    for i in range(w):
        tops[i] = h - tops[i]
    return crates, tops


def parse_moves(lines):
    def parse_move(line):
        parts = line.split()
        return [int(parts[1]), int(parts[3]), int(parts[5])]
    return [parse_move(line) for line in lines]


def apply_move(crates, tops, m, reverse):
    (n, src, dst) = m
    src -= 1
    dst -= 1
    w = len(tops)
    ts = tops[src]
    td = tops[dst]
    for i in range(n):
        ps = ts - i - 1
        pd = td + i if reverse else td + n - i - 1
        while len(crates) <= pd:
            crates.append([' '] * w)
        crates[pd][dst] = crates[ps][src]
        crates[ps][src] = ' '
    tops[src] -= n
    tops[dst] += n


def eval_crates(data, reverse):
    parts = [s.split("\n") for s in data.split("\n\n")]
    crates, tops = parse_crates(parts[0][:-1])
    moves = parse_moves(parts[1])
    for m in moves:
        apply_move(crates, tops, m, reverse)

    return ''.join(crates[tops[i] - 1][i] for i in range(len(tops)))


def solution():
    data = open("../data/05.txt").read()

    res1, res2 = [eval_crates(data, r) for r in [True, False]]
    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
