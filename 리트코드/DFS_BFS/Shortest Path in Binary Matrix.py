from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        def bfs():
            while queue:
                x, y = queue.popleft()
                visited[x][y] = True
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == True or grid[nx][ny] == 1:
                        continue
                    grid[nx][ny] = grid[x][y] + 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))                
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        if grid == [[0]]:
            return 1
        
        n = len(grid)
        queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        dx = [-1, 1, 0, 0, -1, 1, -1, 1]
        dy = [0, 0, -1, 1, -1, 1, 1, -1]
        
        bfs()
        
        if grid[-1][-1] == 0:
            return -1
        else:
            return grid[-1][-1] + 1
    
a = Solution()
print(a.shortestPathBinaryMatrix([[0,1,1,0,0,0],[0,1,0,1,1,0],[0,1,1,0,1,0],[0,0,0,1,1,0],[1,1,1,1,1,0],[1,1,1,1,1,0]]))