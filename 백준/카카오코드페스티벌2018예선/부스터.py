import sys, heapq
input = sys.stdin.readline

N, Q = map(int, input().split())
checkpoint = [tuple(map(int, input().split())) for _ in range(N)]
question = [tuple(map(int, input().split())) for _ in range(Q)]

ans = []
for q in question:
    res = None
    hp = q[2]
    pos = checkpoint[q[0] - 1]
    goal = checkpoint[q[1] - 1]
    visited = [False] * N
    visited[q[0] - 1] = True
    
    while pos != goal:
        if hp == 0 and pos not in checkpoint:
            res = 'NO'
            break
        elif pos[0] == goal[0] or pos[1] == goal[1]:
            res = 'YES'
            break
        else:
            flag = False
            tmp = []
            for i in checkpoint:
                heapq.heappush(tmp, (((((pos[0] - i[0]) ** 2) + ((pos[1] + i[1]) ** 2))) ** 0.5, i))
            for i in range(len(tmp)):
                if visited[i] == True:
                    continue
                if tmp[i][1][0] == pos[0] or tmp[i][1][1] == pos[1]:
                    pos = tmp[i][1]
                    visited[i] = True
                    flag = True
                    break
                else:
                    if abs(pos[0] - tmp[i][1][0]) <= hp or abs(pos[1] - tmp[i][1][1]) <= hp:
                        pos = tmp[i][1]
                        visited[i] = True
                        flag = True
                        break
            if flag == False:
                res = 'NO'
                break
    ans.append(res)
print(ans)