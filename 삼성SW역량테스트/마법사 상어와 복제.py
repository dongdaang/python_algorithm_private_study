def p(a):
    for i in range(4):
        print(a[i])
    print('\n')

def dfs(x, y, c, f, a, b):
    global fish
    global tmp2
    global shark_road
    s = ''.join(str(j) for j in b)
    if c == 3:
        if f > fish:
            shark_road = a[:]
            fish = f
            tmp2 = int(s)
            return
        elif f == fish:
            if int(s) < tmp2:
                shark_road = a[:]
                tmp2 = int(s)
                return
        return
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or s in road_check:
            continue
        road_check.append(s)
        dfs(nx, ny, c + 1, f + len(new_grid[nx][ny]), a + [(nx, ny)], b + [i + 1])

M, S = map(int, input().split())
grid = [list([] for _ in range(4)) for _ in range(4)]
smell_grid = [[0] * 4 for _ in range(4)]
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(M):
    fx, fy, d = map(int, input().split())
    grid[fx - 1][fy - 1].append(d - 1)
sx, sy = map(int, input().split())
sx -= 1
sy -= 1

for _ in range(S):
    new_grid = [list([] for _ in range(4)) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if grid[i][j]:
                for d in grid[i][j]:
                    cnt = 0
                    tmp = d
                    while True:
                        if cnt == 8:
                            new_grid[i][j].append(d)
                            break
                        nx = i + dx[tmp]
                        ny = j + dy[tmp]
                        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                            tmp = (tmp + 7) % 8
                            cnt += 1
                        elif (nx, ny) == (sx, sy) or smell_grid[nx][ny]:
                            tmp = (tmp + 7) % 8
                            cnt += 1
                        else:
                            new_grid[nx][ny].append(tmp)
                            break
    p(new_grid)
    global fish
    global tmp2
    global shark_road
    fish = 0
    tmp2 = 445
    shark_road = []
    road_check = []
    visited = [[False] * 4 for _ in range(4)]
    dfs(sx, sy, 0, 0, [], [])

    for i in range(4):
        for j in range(4):
            if smell_grid[i][j] > 0:
                smell_grid[i][j] -= 1

    for road in shark_road:
        if new_grid[road[0]][road[1]]:
            new_grid[road[0]][road[1]] = []
            smell_grid[road[0]][road[1]] = 2

    sx, sy = shark_road[-1][0], shark_road[-1][1]

    for i in range(4):
        for j in range(4):
            grid[i][j] += new_grid[i][j]

    print(fish)
    print(tmp2)
    print(shark_road)
    print('\n')

    p(grid)

res = 0
for i in range(4):
    for j in range(4):
        if grid[i][j]:
            res += len(grid[i][j])


print(res)