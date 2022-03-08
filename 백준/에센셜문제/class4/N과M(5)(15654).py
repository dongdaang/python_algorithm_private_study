import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
res = []

def f():
    if len(res) == M:
        print(' '.join(map(str, res)))
    else:
        for i in nums:
            if i in res:
                continue
            res.append(i)
            f()
            res.pop()

if M == 1:
    for i in nums:
        print(i)
else:
    f()