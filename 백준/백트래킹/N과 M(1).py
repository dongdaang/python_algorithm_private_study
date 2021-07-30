N, M = map(int, input().split())

num = []

def f():
    if len(num) == M:
        print(' '.join(map(str, num)))
        return

    for i in range(1, N+1):
        if i in num:
            continue
        num.append(i)
        f()
        num.pop()
f()

# from itertools import permutations
# N,M = map(int, input().split(' '))
# print('\n'.join(list(map(' '.join, permutations(map(str, range(1, N+1)),M)))))