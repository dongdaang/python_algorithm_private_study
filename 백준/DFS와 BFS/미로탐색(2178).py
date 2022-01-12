from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

def bfs(x, y):
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

      if graph[nx][ny] == 0:
        continue
      
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  return graph[N-1][M-1]

print(bfs(0, 0))


# 정답예시 코드
# n,m = map(int, input().split())
# s = []
# for _ in range(n):
#     s.append(list(input()))

# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
# queue = [[0,0]]
# s[0][0] = 1
# while queue:
#     a,b = queue[0][0], queue[0][1]
#     del queue[0]
#     for i in range(4):
#         x = a+dx[i]
#         y = b+dy[i]
#         if 0<=x<n and 0<=y<m and s[x][y] == '1':
#             queue.append([x,y])
#             s[x][y] = s[a][b] + 1
# print(s[n-1][m-1])