import sys
input = sys.stdin.readline

N = int(input())
scores = []
for _ in range(N):
    scores.append(list(map(int, input().split())))
scores.sort(key=lambda x : x[0])

winner = []

for i in range(1, 5):
    M = -1
    num = 0
    for j in range(N):
        if scores[j][i] > M and j + 1 not in winner:
            M = scores[j][i]
            num = j + 1
    winner.append(num)

for i in winner:
    print(i, end=' ')