class Solution:
    def islandPerimeter(self, grid):
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def dfs(x, y):
            cnt = 4
            visited[x][y] = 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                    if grid[nx][ny] == 1:
                        cnt -= 1
                    if visited[nx][ny] == 0 and grid[nx][ny] == 1:
                        dfs(nx, ny)
            return cnt
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans += dfs(i, j)
        return ans

a = Solution()
print(a.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))