import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    coordinate = list(map(int, input().split()))
    x1, y1 = coordinate[0], coordinate[1]
    x2, y2 = coordinate[2], coordinate[3]
    for i in range(M-y2, M-y1):
        for j in range(x1, x2):
            if graph[i][j] == 0:
                graph[i][j] = 1
space = 0
def dfs(x, y):
    global space
    if graph[x][y] == 0:
        graph[x][y] = 1
        space += 1
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < M and ny >= 0 and ny < N:
                dfs(nx, ny)
    return space
total_space = []
for i in range(M):
    for j in range(N):
        if dfs(i, j) != 0:
            total_space.append(dfs(i, j))
            space = 0
total_space.sort()
print(len(total_space))
print(total_space)