class Solution:
    def maxAreaOfIsland(self, grid):
        island = []
        global area
        area = 0
        
        def dfs(x, y):
            global area
            grid[x][y] = 0
            area = area + 1
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != 1:
                    continue
                dfs(nx, ny)
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    island.append(area)
                    area = 0
        if not island:
            return 0
        else:
            return max(island)

a = Solution()
print(a.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))