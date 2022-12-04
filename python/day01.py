def solution():
    data = open("../data/01.txt").read()
    cals = [[int(y) for y in x.split("\n")]
            for x in data.split("\n\n")]

    res1 = max(sum(s) for s in cals)
    res2 = sum(sorted(sum(s) for s in cals)[-3:])

    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
