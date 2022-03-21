from collections import deque

class Solution:
    def solve(self, board):
        def bfs(i, j):
            tmp = [(i, j)]
            queue = deque([(i, j)])
            visited[i][j] = True
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny] == True or board[nx][ny] == 'X':
                        continue
                    tmp.append((nx, ny))
                    visited[nx][ny] = True
                    queue.append((nx, ny))
            res.append(tmp)
            
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        res = []
        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == 'O' and not visited[i][j]:
                    bfs(i, j)
        
        for i in range(len(res)):
            for x, y in res[i]:
                if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                    res[i] = []
                    break
        
        for i in range(len(res)):
            if res[i]:
                for x, y in res[i]:
                    board[x][y] = 'X'
        
a = Solution()
print(a.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))