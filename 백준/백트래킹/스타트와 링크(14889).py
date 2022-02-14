import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

teams = []
result = 10000
visited = [0] * (N + 1)

def dfs():
    global result
    if len(teams) == N // 2:
        sum1 = 0
        sum2 = 0
        tmp = []
        for i in teams:
            for j in teams:
                if i != j:
                    sum1 += graph[i-1][j-1]
        for i in range(1, len(visited)):
            if visited[i] == 0:
                tmp.append(i)
        for i in tmp:
            for j in tmp:
                if i != j:
                    sum2 += graph[i-1][j-1]
        if abs(sum1 - sum2) < result:
            result = abs(sum1 - sum2)
        return
    
    for i in range(1, N + 1):
        if teams == [2]:
            break
        if i not in teams:
            teams.append(i)
            visited[i] = 1
            dfs()
            a = teams.pop()
            visited[a] = 0

dfs()
print(result)