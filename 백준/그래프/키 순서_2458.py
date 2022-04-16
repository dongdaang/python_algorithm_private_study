import sys
input = sys.stdin.readline

def floydWashall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j]:
                    continue
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
res = [0] * N
ans = 0

floydWashall()

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            res[i] += 1
            res[j] += 1
        
for i in range(N):
    if res[i] == N - 1:
        ans += 1
        
print(ans)