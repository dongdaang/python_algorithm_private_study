import sys
input = sys.stdin.readline

N = int(input())
square = []
result = []
for _ in range(N):
    a = list(map(int, input().split()))
    square.append(a)

def cut(x, y, N):
    c = square[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if c != square[i][j]:
                cut(x, y, N//2)
                cut(x, y+N//2, N//2)
                cut(x+N//2, y, N//2)
                cut(x+N//2, y+N//2, N//2)
                return
    if c == 0:
        result.append(0)
    else:
        result.append(1)

cut(0, 0, N)
print(result.count(0))
print(result.count(1))