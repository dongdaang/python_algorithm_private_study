def solution(places):
    answer = []
    for place in places:
        c = []
        tmp_2 = 0
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    c.append([i, j])
        for i in range(len(c)-1):
            tmp = 0
            for j in range(i+1, len(c)):
                if (abs(c[i][0] - c[j][0]) + abs(c[i][1] - c[j][1])) == 1:
                    tmp = 1
                    break
                elif (abs(c[i][0] - c[j][0]) + abs(c[i][1] - c[j][1])) == 2:
                    if c[i][0] == c[j][0]:
                        if place[c[i][0]][(c[i][1]+c[j][1])//2] != 'X':
                            tmp = 1
                            break
                    elif c[i][1] == c[j][1]:
                        if place[(c[i][0]+c[j][0])//2][c[i][1]] != 'X':
                            tmp = 1
                            break
                    else:
                        if place[c[i][0]][c[j][1]] != 'X' or place[c[j][0]][c[i][1]] != 'X':
                            tmp = 1
                            break
            if tmp == 1:
                answer.append(0)
                tmp_2 = 1
                break
        if tmp_2 == 0:
            answer.append(1)
    return answer