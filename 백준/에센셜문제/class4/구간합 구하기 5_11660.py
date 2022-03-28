import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

for i in range(1, N + 1):
    for j in range(2, N + 1):
        graph[i][j] += graph[i][j - 1]
for i in range(1, N + 1):
    for j in range(2, N + 1):
        graph[j][i] += graph[j - 1][i]
res = []

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res.append(graph[x2][y2] - graph[x2][y1 - 1] - graph[x1 - 1][y2] + graph[x1 - 1][y1 - 1])

for i in res:
    print(i)