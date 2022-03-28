import sys
input = sys.stdin.readline

matrix1 = []
matrix2 = []

N1, M1 = map(int, input().split())
for _ in range(N1):
    matrix1.append(list(map(int, input().split())))
N2, M2 = map(int, input().split())
for _ in range(N2):
    matrix2.append(list(map(int, input().split())))

result = [[0 for _ in range(M2)] for _ in range(N1)]

def cut(a):
    tmp = [[] for _ in range(M2)]
    for i in range(M2):
        for j in range(N2):
            tmp[i].append(a[j][i])
    return tmp

new_matrix2 = cut(matrix2)
r = 0
c = 0

while r < N1:
    for i in matrix1:
        for j in new_matrix2:
            sum = 0
            for k in range(len(i)):
                sum += i[k] * j[k]
            result[r][c] = sum
            c += 1
        r += 1
        c = 0

for i in range(N1):
    for j in range(M2):
        print(result[i][j], end=' ')