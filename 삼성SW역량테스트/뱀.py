import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
apple_location = []
for _ in range(K):
    a, b = map(int, input().split())
    apple_location.append((a - 1, b - 1))
L = int(input())
turning_info = []
for _ in range(L):
    X, C = input().split()
    turning_info.append((int(X), C))
time = 0
snake = [(0, 0)]
move = (0, 1)
turning_info.reverse()
turning = turning_info.pop()
while True:
    time += 1
    nx = snake[0][0] + move[0]
    ny = snake[0][1] + move[1]
    if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in snake:
        break
    elif (nx, ny) in apple_location:
        apple_location.remove((nx, ny))
        snake  = [(nx, ny)] + snake
    else:
        snake.pop()
        snake = [(nx, ny)] + snake

    if turning[0] == time:
        if turning[1] == 'D':
            if move == (0, 1):
                move = (1, 0)
            elif move == (1, 0):
                move = (0, -1)
            elif move == (0, -1):
                move = (-1, 0)
            else:
                move = (0, 1)
        else:
            if move == (0, 1):
                move = (-1, 0)
            elif move == (-1, 0):
                move = (0, -1)
            elif move == (0, -1):
                move = (1, 0)
            else:
                move = (0, 1)
        if turning_info:
            turning = turning_info.pop()

print(time)