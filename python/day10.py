# DAY10
def eval_ops(lines):
    ip, x = 1, 1
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "noop":
            yield (ip, x, 1)
            ip += 1
        elif parts[0] == "addx":
            d = int(parts[1])
            yield (ip, x, 2)
            ip += 2
            x += d


def acc_res(ip, x, nnext):
    for f in range(20, 260, 40):
        if ip <= f and ip + nnext > f:
            return f * x
    return 0


WIDTH, HEIGHT = 40, 6


def set_display(d, ip, x, nnext):
    for i in range(nnext):
        pos = ip - 1 + i
        k = pos % WIDTH
        c = "#" if k >= x - 1 and k <= x + 1 else "."
        px, py = pos % WIDTH, int(pos / WIDTH)
        d[py][px] = c


def solution():
    lines = [s.strip() for s in open("../data/10.txt").readlines()]

    res1 = sum(acc_res(ip, x, n) for (ip, x, n) in eval_ops(lines))

    display = [[' '] * WIDTH for _ in range(HEIGHT)]
    for (ip, x, n) in eval_ops(lines):
        set_display(display, ip, x, n)
    res2 = '\n'.join(''.join(s) for s in display)
    print(f'Answer 1: {res1}\nAnswer 2: \n{res2}')
