import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

##############DFS풀이#############
T = int(input())
ans = []
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    
    def dfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        if graph[x][y] == 1:
            graph[x][y] = 0
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx >= 0 and nx < N and ny >= 0 and ny < M:
                    dfs(nx, ny)
            return True
        return False
    
    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j) == True:
                result += 1
    ans.append(result)

for i in ans:
    print(i)
    
##############BFS풀이#############
T = int(input())
ans = []
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    
    def bfs(x, y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        queue = deque([[x, y]])

        while queue:
            a, b = queue.popleft()
            for i in range(4):
                c = a + dx[i]
                d = b + dy[i]
                if c >= 0 and c < N and d >= 0 and d < M and graph[c][d] == 1:
                    graph[c][d] = 0
                    queue.append([c, d])
    
    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                graph[i][j] = 0
                result += 1
    ans.append(result)
    
for i in ans:
    print(i)