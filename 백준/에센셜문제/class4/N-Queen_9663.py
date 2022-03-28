N = int(input())

res = 0
col = [0] * N

def possible(x):
    for i in range(x):
        if col[i] == col[x] or abs(col[i] - col[x]) == abs(i - x):
            return False
    return True

def n_queens(x):
    global res
    
    if x == N:
        res += 1
    else:
        for i in range(N):
            col[x] = i
            if possible(x):
                n_queens(x + 1)

n_queens(0)
print(res)