import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

res = 1
visited = [False] * (N + 1)

def dfs(a):
    global cnt
    cnt += 1
    visited[a] = True
    for i in graph[a]:
        if visited[i] == True:
            continue
        dfs(i)

for i in range(len(graph)):
    cnt = 0
    if graph[i] and visited[i] == False:
        dfs(i)
        res *= cnt

print(res % 1000000007)