def roll(d):
    if d == 0:
        tmp1 = dice[1].pop()
        tmp2 = dice[3][1]
        dice[1] = [tmp2] + dice[1]
        dice[3][1] = tmp1

    if d == 1:
        tmp = [dice[i][1] for i in range(4)]
        for i in range(4):
            dice[(i + 1) % 4][1] = tmp[i]

    if d == 2:
        tmp1 = dice[1].pop(0)
        tmp2 = dice[3][1]
        dice[1].append(tmp2)
        dice[3][1] = tmp1

    if d == 3:
        tmp = [dice[i][1] for i in range(4)]
        for i in range(3, -1, -1):
            dice[i - 1][1] = tmp[i]

def move(d):
    nx = x + dx[d]
    ny = y + dy[d]
    if nx < 0 or nx >= N or ny < 0 or ny >= M:
        d = (d + 2) % 4
        return x + dx[d], y + dy[d], d
    else:
        return x + dx[d], y + dy[d], d

def direction(d):
    A, B = dice[3][1], board[x][y]

    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (d + 3) % 4

    return d

def score(a, b):
    queue = [(a, b)]
    visited = [[False] * M for _ in range(N)]
    visited[a][b] = True
    C = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
                continue
            if board[nx][ny] == board[x][y]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                C += 1

    return board[a][b] * C

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
x, y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
d = 0
point = 0

for _ in range(K):
    x, y, d = move(d)
    roll(d)
    point += score(x, y)
    d = direction(d)

print(point)