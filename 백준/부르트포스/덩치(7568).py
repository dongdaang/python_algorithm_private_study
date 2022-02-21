import sys
input = sys.stdin.readline

N = int(input())
infos = []
for _ in range(N):
    infos.append(tuple(map(int, input().split())))

for i in infos:
    rank = 1
    for j in infos:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')