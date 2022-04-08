import sys
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [[0] * (m + 1)]
for _ in range(n):
    grid.append([0] + list(map(int, input().rstrip())))

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if grid[i][j] >= 1:
            grid[i][j] = min(grid[i - 1][j - 1], grid[i][j - 1], grid[i - 1][j]) + 1
print(max(max(grid[i]) for i in range(1, n + 1)) ** 2)