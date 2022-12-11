from dataclasses import dataclass
from enum import Enum
from typing import List


class OpType(Enum):
    ADD = 1
    MUL = 2
    SQUARE = 3


@dataclass
class MonkeyOp:
    idx: int
    start_items: List[int]
    op: OpType
    op_arg: int
    test_arg: int
    true_target: int
    false_target: int


def parse_op(data):
    lines = data.split("\n")
    parts = lines[0][:-1].split(" ")
    idx = int(parts[1])
    start_items = [int(x) for x in lines[1].split(":")[1].split(",")]
    parts = lines[2].split("= ")[1].split(" ")
    op = OpType.ADD if parts[1] == "+" else OpType.MUL
    op_arg = 0
    if parts[2] == "old":
        op = OpType.SQUARE
    else:
        op_arg = int(parts[2])
    test_arg = int(lines[3].split(" ")[-1])
    true_target = int(lines[4].split(" ")[-1])
    false_target = int(lines[5].split(" ")[-1])
    return MonkeyOp(idx, start_items, op, op_arg, test_arg, true_target, false_target)


def step(ops, items, inspect_counts, reduce_worry_level):
    n = len(ops)
    den = 1
    for op in ops:
        den *= op.test_arg
    for i in range(n):
        op = ops[i]
        it = items[i]
        inspect_counts[i] += len(it)
        for worry_level in it:
            if op.op == OpType.ADD:
                worry_level = worry_level + op.op_arg
            elif op.op == OpType.MUL:
                worry_level = worry_level * op.op_arg
            else:
                worry_level *= worry_level
            if reduce_worry_level:
                worry_level = int(worry_level / 3)
            worry_level = worry_level % den
            target = op.true_target if worry_level % op.test_arg == 0 else op.false_target
            items[target].append(worry_level)
        items[i] = []


def eval_steps(ops, n, reduce_worry_level):
    items = [op.start_items.copy() for op in ops]
    inspect_counts = [0] * len(ops)

    for i in range(n):
        step(ops, items, inspect_counts, reduce_worry_level)

    s = sorted(inspect_counts)
    return s[-1] * s[-2]


def solution():
    ops = [parse_op(s) for s in open("../data/11.txt").read().split("\n\n")]
    res1 = eval_steps(ops, 20, True)
    res2 = eval_steps(ops, 10000, False)

    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
