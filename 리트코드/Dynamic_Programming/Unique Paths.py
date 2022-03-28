from collections import deque

class Solution:
    def uniquePaths(self, m, n):
        def bfs():
            while queue:
                x, y = queue.popleft()
                for i in range(2):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx >= m or ny >= n:
                        continue
                    grid[nx][ny] += grid[x][y]
                    if (nx, ny) not in queue:
                        queue.append((nx, ny))
                    
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1
        dx = [1, 0]
        dy = [0, 1]
        queue = deque([(0, 0)])
        bfs()
        
        return grid[-1][-1]
        
a = Solution()
print(a.uniquePaths(3, 7))