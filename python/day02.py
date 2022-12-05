def solution():
    data = [s.strip().split() for s in open("../data/02.txt").readlines()]

    scores1 = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    scores2 = {
        ('A', 'X'): 3,
        ('B', 'X'): 0,
        ('C', 'X'): 6,
        ('A', 'Y'): 6,
        ('B', 'Y'): 3,
        ('C', 'Y'): 0,
        ('A', 'Z'): 0,
        ('B', 'Z'): 6,
        ('C', 'Z'): 3,
    }

    move_mapping = {
        ('A', 'X'): 'Z',
        ('B', 'X'): 'X',
        ('C', 'X'): 'Y',
        ('A', 'Y'): 'X',
        ('B', 'Y'): 'Y',
        ('C', 'Y'): 'Z',
        ('A', 'Z'): 'Y',
        ('B', 'Z'): 'Z',
        ('C', 'Z'): 'X',
    }

    def get_score1(a, b):
        return scores1[b] + scores2[(a, b)]

    def get_score2(a, b):
        move = move_mapping[(a, b)]
        return scores1[move] + scores2[(a, move)]

    res1 = sum(get_score1(a, b) for (a, b) in data)
    res2 = sum(get_score2(a, b) for (a, b) in data)

    print(f'Answer 1: {res1}\nAnswer 2: {res2}')
