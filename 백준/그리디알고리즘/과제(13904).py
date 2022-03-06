import sys
input = sys.stdin.readline

N = int(input())
hw = [tuple(map(int, input().split())) for _ in range(N)]
hw.sort()
tmp = []
date = hw[-1][0]
res = 0
while True:
    if date == 0:
        break
    while hw and hw[-1][0] >= date:
        tmp.append(hw.pop()[1])
    date -= 1
    if not tmp:
        continue
    tmp.sort()
    res += tmp.pop()
print(res)