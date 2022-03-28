import sys
input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def possible(a):
    visited = [[False] * N for _ in range(N)]
    for i in range(N - 1):
        if a[i] == a[i + 1]:
            continue
        if abs(a[i] - a[i + 1]) > 1:
            return False
        if a[i] > a[i + 1]:
            now = a[i + 1]
            for j in range(i + 1, i + 1 + L):
                if j < 0 or j >= N:
                    return False
                if a[j] != now:
                    return False
                if visited[j] == True:
                    return False
                visited[j] = True
        else:
            now = a[i]
            for j in range(i, i - L, -1):
                if j < 0 or j >= N:
                    return False
                if a[j] != now:
                    return False
                if visited[j] == True:
                    return False
                visited[j] = True
    return True

res = 0

for i in range(N):
    if possible(graph[i]):
        res += 1
    tmp = [graph[j][i] for j in range(N)]
    if possible(tmp):
        res += 1

print(res)