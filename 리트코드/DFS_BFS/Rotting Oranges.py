from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        flag1 = False
        flag2 = False
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    flag1 = True
                    grid[i][j] = -1
        
        if flag1 == False:
            return 0
        
        while queue:
            x, y = queue.popleft()
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] != -1:
                    continue
                grid[nx][ny] = grid[x][y] + 1
                queue.append((nx, ny))

        max = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    flag2 = True
                    break
                else:
                    if grid[i][j] > max:
                        max = grid[i][j]
        
        if flag2 == True:
            return -1
        else:
            return max - 2

a = Solution()
print(a.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))