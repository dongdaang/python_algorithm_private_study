def bfs(a, b):
    queue = [(a, b)]
    visited[a][b] = True
    rainbow_blocks = []
    normal_blocks = [(a, b)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                continue

            if grid[nx][ny] == 0:
                rainbow_blocks.append((nx, ny))
                visited[nx][ny] = True
                queue.append((nx, ny))

            elif grid[nx][ny] == color:
                normal_blocks.append((nx, ny))
                visited[nx][ny] = True
                queue.append((nx, ny))

    return (normal_blocks, rainbow_blocks)

def gravity():
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if grid[i][j] == -1 or grid[i][j] == -2:
                continue
            r = i
            tmp = grid[i][j]
            flag = False
            while r < N - 1 and grid[r + 1][j] == -2:
                r += 1
                flag = True
            if flag:
                grid[r][j] = tmp
                grid[i][j] = -2

def rotate():
    new_grid = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_grid[i][j] = grid[j][N - 1 - i]

    return new_grid

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
point = 0

while True:
    visited = [[False] * N for _ in range(N)]
    color = 0
    max_block = (None, 0, 0)
    max_total_blocks = None

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and grid[i][j] > 0:
                color = grid[i][j]
                total_normal_blocks, total_rainbow_blocks = bfs(i, j)
                for x, y in total_rainbow_blocks:
                    visited[x][y] = False
                total_blocks = total_normal_blocks + total_rainbow_blocks
                n = len(total_blocks)
                rainbow_cnt = len(total_rainbow_blocks)

                if n > max_block[1]:
                    max_total_blocks = total_blocks[:]
                    max_block = ((i, j), n, rainbow_cnt)

                elif n == max_block[1]:
                    if rainbow_cnt > max_block[2]:
                        max_total_blocks = total_blocks[:]
                        max_block = ((i, j), n, rainbow_cnt)

                    elif rainbow_cnt == max_block[2]:
                        if i > max_block[0][0]:
                            max_total_blocks = total_blocks[:]
                            max_block = ((i, j), n, rainbow_cnt)

                        elif total_normal_blocks[0][0] == max_block[0][0]:
                            if j > max_block[0][1]:
                                max_total_blocks = total_blocks[:]
                                max_block = ((i, j), n, rainbow_cnt)

    if max_block[1] < 2:
        break

    point += max_block[1] ** 2

    for i in range(N):
        for j in range(N):
            if (i, j) in max_total_blocks:
                grid[i][j] = -2

    gravity()
    tmp2 = rotate()
    grid = [tmp2[i][:] for i in range(N)]
    gravity()

print(point)