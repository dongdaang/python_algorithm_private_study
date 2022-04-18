import sys
from itertools import combinations
input = sys.stdin.readline

def enemy_move():
    for i in range(M):
        if grid_tmp[N - 1][i] == 1:
            grid_tmp[N - 1][i] = 0
            
    for i in range(N - 2, -1, -1):
        for j in range(M):
            if grid_tmp[i][j] == 1:
                grid_tmp[i][j] = 0
                grid_tmp[i + 1][j] = 1

def attack_bounds(pos):
    can_attack = []
    for i in range(N):
        for j in range(M):
            if (grid_tmp[i][j] == 1 or grid_tmp[i][j] == -1) and abs(pos[0] - i) + abs(pos[1] - j) <= D:
                can_attack.append(((i, j), abs(pos[0] - i) + abs(pos[1] - j)))
    if can_attack:
        can_attack.sort(key=lambda x : (x[1], x[0][1]))
        return can_attack[0][0]
    else:
        return False

def archer_attack(pos):
    target = attack_bounds(pos)
    if target:
        grid_tmp[target[0]][target[1]] = -1

def enemy_check():
    kill_cnt = 0
    for i in range(N):
        for j in range(M):
            if grid_tmp[i][j] == -1:
                grid_tmp[i][j] = 0
                kill_cnt += 1
    
    return kill_cnt

N, M, D = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
archers = list(combinations((i for i in range(M)), 3))
grid_check = [[0] * M for _ in range(N)]
res = 0

for archer in archers:
    grid_tmp = [grid[i][:] for i in range(N)]
    total = 0
    archer_pos = [(N, i) for i in archer]
    while grid_tmp != grid_check:
        for pos in archer_pos:
            archer_attack(pos)
        total += enemy_check()
        enemy_move()
    
    if total > res:
        res = total

print(res)