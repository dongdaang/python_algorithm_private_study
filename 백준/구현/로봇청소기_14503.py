import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0

while True:
    cnt += 1
    visited[r][c] = 1
    while True:
        flag = False
        if d == 0:
            if (graph[r - 1][c] == 1 or visited[r - 1][c] == 1) and graph[r + 1][c] == 1 and \
                (graph[r][c - 1] == 1 or visited[r][c - 1] == 1) and (graph[r][c + 1] == 1 or visited[r][c + 1] == 1):
                    flag = True
                    break
            elif (graph[r - 1][c] == 1 or visited[r - 1][c] == 1) and visited[r + 1][c] == 1 and \
                (graph[r][c - 1] == 1 or visited[r][c - 1] == 1) and (graph[r][c + 1] == 1 or visited[r][c + 1] == 1):
                    r += 1
                    continue
            elif graph[r][c - 1] == 1 or visited[r][c - 1] == 1:
                d = 3
                continue
            else:
                c -= 1
                d = 3
                break
        elif d == 1:
            if (graph[r - 1][c] == 1 or visited[r - 1][c] == 1) and (graph[r + 1][c] == 1 or visited[r + 1][c] == 1) and \
                graph[r][c - 1] == 1 and (graph[r][c + 1] == 1 or visited[r][c + 1] == 1):
                    flag = True
                    break
            elif (graph[r - 1][c] == 1 or visited[r - 1][c] == 1) and (graph[r + 1][c] == 1 or visited[r + 1][c] == 1) and \
                visited[r][c - 1] == 1 and (graph[r][c + 1] == 1 or visited[r][c + 1] == 1):
                    c -= 1
                    continue
            elif graph[r - 1][c] == 1 or visited[r - 1][c] == 1:
                d = 0
                continue
            else:
                r -= 1
                d = 0
                break
        elif d == 2:
            if graph[r - 1][c] == 1 and (graph[r + 1][c] == 1 or visited[r + 1][c] == 1) and \
                (graph[r][c - 1] == 1 or visited[r][c - 1] == 1) and (graph[r][c + 1] == 1 or visited[r][c + 1] == 1):
                    flag = True
                    break
            elif visited[r - 1][c] == 1 and (graph[r + 1][c] == 1 or visited[r + 1][c] == 1) and \
                (graph[r][c - 1] == 1 or visited[r][c - 1] == 1) and (graph[r][c + 1] == 1 or visited[r][c + 1] == 1):
                    r -= 1
                    continue
            elif graph[r][c + 1] == 1 or visited[r][c + 1] == 1:
                d = 1
                continue
            else:
                c += 1
                d = 1
                break
        else:
            if (graph[r - 1][c] == 1 or visited[r - 1][c] == 1) and (graph[r + 1][c] == 1 or visited[r + 1][c] == 1) and \
                (graph[r][c - 1] == 1 or visited[r][c - 1] == 1) and graph[r][c + 1] == 1:
                    flag = True
                    break
            elif (graph[r - 1][c] == 1 or visited[r - 1][c] == 1) and (graph[r + 1][c] == 1 or visited[r + 1][c] == 1) and \
                (graph[r][c - 1] == 1 or visited[r][c - 1] == 1) and visited[r][c + 1] == 1:
                    c += 1
                    continue
            elif graph[r + 1][c] == 1 or visited[r + 1][c] == 1:
                d = 2
                continue
            else:
                r += 1
                d = 2
                break
    if flag == True:
        break

print(cnt)