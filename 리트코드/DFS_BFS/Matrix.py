from collections import deque

class Solution:
    def updateMatrix(self, mat):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1
        
        def bfs():
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or mat[nx][ny] != -1:
                        continue
                    mat[nx][ny] = mat[x][y] + 1
                    queue.append((nx, ny))
        
        bfs()
        return mat
    
a = Solution()
print(a.updateMatrix([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]))