from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited = [[0] * len(image[0]) for i in range(len(image))]
        origin = image[sr][sc]
        
        def bfs():
            queue = deque()
            queue.append((sr, sc))
            
            while queue:
                x, y = queue.popleft()
                image[x][y] = newColor
                visited[x][y] = 1
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= len(image) or ny < 0 or ny >= len(image[0]) or image[nx][ny] != origin or visited[nx][ny] == 1:
                        continue
                    queue.append((nx, ny))
        bfs()
        return image

a = Solution()
print(a.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))