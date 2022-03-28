import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def up():
    for i in range(N):
        line = [board[j][i] for j in range(N)]
        tmp1 = []
        tmp2 = []
        for num in line:
            if num != 0:
                tmp1.append(num)
        if not tmp1:
            continue
        for k in range(len(tmp1) - 1):
            if tmp1[k] == tmp1[k + 1]:
                tmp1[k] *= 2
                tmp1[k + 1] = 0
        for num in tmp1:
            if num != 0:
                tmp2.append(num)
        for k in range(len(tmp2)):
            board[k][i] = tmp2[k]
        for k in range(len(tmp2), N):
            board[k][i] = 0
        
def down():
    for i in range(N):
        line = [board[j][i] for j in range(N)]
        tmp1 = []
        tmp2 = []
        for num in line:
            if num != 0:
                tmp1.append(num)
        if not tmp1:
            continue
        for k in range(len(tmp1) - 1, 0, -1):
            if tmp1[k] == tmp1[k - 1]:
                tmp1[k] *= 2
                tmp1[k - 1] = 0
        for num in tmp1:
            if num != 0:
                tmp2.append(num)
        l = len(tmp2)
        for k in range(N - 1, N - len(tmp2) - 1, -1):
            board[k][i] = tmp2.pop()
        for k in range(N - l - 1, -1, -1):
            board[k][i] = 0

def left():
    for i in range(N):
        line = board[i]
        tmp1 = []
        tmp2 = []
        for num in line:
            if num != 0:
                tmp1.append(num)
        if not tmp1:
            continue
        for k in range(len(tmp1) - 1):
            if tmp1[k] == tmp1[k + 1]:
                tmp1[k] *= 2
                tmp1[k + 1] = 0
        for num in tmp1:
            if num != 0:
                tmp2.append(num)
        for k in range(len(tmp2)):
            board[i][k] = tmp2[k]
        for k in range(len(tmp2), N):
            board[i][k] = 0

def right():
    for i in range(N):
        line = board[i]
        tmp1 = []
        tmp2 = []
        for num in line:
            if num != 0:
                tmp1.append(num)
        if not tmp1:
            continue
        for k in range(len(tmp1) - 1, 0, -1):
            if tmp1[k] == tmp1[k - 1]:
                tmp1[k] *= 2
                tmp1[k - 1] = 0
        for num in tmp1:
            if num != 0:
                tmp2.append(num)
        l = len(tmp2)
        for k in range(N - 1, N - len(tmp2) - 1, -1):
            board[i][k] = tmp2.pop()
        for k in range(N - l - 1, -1, -1):
            board[i][k] = 0

def back_tracking(x):
    up()
    down()
    right()
    left()