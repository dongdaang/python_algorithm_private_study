class Solution:
    def gameOfLife(self, board):
        def check(x, y):
            live_cell = 0
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if board[nx][ny] == 1:
                        live_cell += 1
                        
            if board[x][y] == 1:
                if live_cell < 2 or live_cell > 3:
                    new_board[x][y] = 0
            else:
                if live_cell == 3:
                    new_board[x][y] = 1
        
        m = len(board)
        n = len(board[0])
        new_board = [board[i][:] for i in range(m)]
        direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for i in range(m):
            for j in range(n):
                check(i, j)
                
        for i in range(m):
            for j in range(n):
                board[i][j] = new_board[i][j]

a = Solution()
print(a.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))