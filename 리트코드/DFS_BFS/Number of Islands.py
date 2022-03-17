from collections import deque

class Solution:
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = 0
        
        def bfs(i, j):
            queue = deque([(i, j)])
            grid[i][j] = '-1'
            while queue:
                x, y = queue.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != '1':
                        continue
                    queue.append((nx, ny))
                    grid[nx][ny] = '-1'
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        
        return res
    
a = Solution()
print(a.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))