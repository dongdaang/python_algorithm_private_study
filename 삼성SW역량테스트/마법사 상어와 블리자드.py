def magic(d, s):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(1, s + 1):
        nx = r + dx[d - 1] * i
        ny = c + dy[d - 1] * i
        grid[nx][ny] = 0

def move():
    new_bead_list = []
    for bead in beads:
        if bead != 0:
            new_bead_list.append(bead)

    return new_bead_list

def explode():
    global res
    i = 0
    j = 1
    flag = False
    while j < len(beads):
        now = beads[i]
        while beads[j] == now:
            j += 1
            if j == len(beads):
                break
        if j - i >= 4:
            flag = True
            res += now * (j - i)
            for k in range(i, j):
                beads[k] = 0
        i = j
        j = i + 1

    return flag

def change():
    i = 0
    j = 1
    new_bead_list = []
    while j < len(beads):
        now = beads[i]
        while beads[j] == now:
            j += 1
            if j == len(beads):
                break
        new_bead_list.append(j - i)
        new_bead_list.append(now)
        i = j
        j = i + 1

    return new_bead_list

def bead_list_made():
    x, y = N // 2, N // 2
    loop_cnt = 2
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    d = 0
    for dist in range(1, N):
        if dist == N - 1:
            loop_cnt = 3
        for _ in range(loop_cnt):
            for _ in range(dist):
                x += dx[d]
                y += dy[d]
                if grid[x][y] != 0:
                    beads.append(grid[x][y])
            d = (d + 1) % 4

def bead_grid_made():
    A = [[0] * N for _ in range(N)]
    x, y = N // 2, N // 2
    loop_cnt = 2
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    d = 0
    if beads:
        for dist in range(1, N):
            if dist == N - 1:
                loop_cnt = 3
            for _ in range(loop_cnt):
                for _ in range(dist):
                    x += dx[d]
                    y += dy[d]
                    if beads:
                        A[x][y] = beads.pop(0)
                d = (d + 1) % 4

    return A

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
blizzard = [list(map(int, input().split())) for _ in range(M)]
r, c = N // 2, N // 2
beads = []
global res
res = 0

for i in range(M):
    d, s = blizzard[i]
    magic(d, s)
    bead_list_made()
    while explode():
        beads = move()
    beads = change()
    grid = bead_grid_made()

print(res)