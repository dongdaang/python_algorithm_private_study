N = int(input())

snail_list = []
for i in range(N):
    snail_list.append([0] * N)

def snail(a, n, num):                         #a = 시작번호
    for i in range(a, n + 1):                 #n = 끝번호
        snail_list[a][i] = num                #예를 들어 6x6 행렬은 시작번호가 0, 끝번호가 5
        num += 1                              #함수 한번 실행될 때 마다 a는 하나씩 증가, n은 하나씩 감소
    for i in range(a + 1, n + 1):             #a와 n이 같아지거나 1차이가 나게 되면 달팽이 배열 완료
        snail_list[i][n] = num
        num += 1
    for i in range(n - 1, a - 1, -1):
        snail_list[n][i] = num
        num += 1
    for i in range(n - 1, a, -1):
        snail_list[i][a] = num
        num += 1
    if n == a or n - a == 1:
        for i in range(N):
            print(snail_list[i])
    else:
        return snail(a + 1, n - 1, num)

snail(0, N - 1, 1)