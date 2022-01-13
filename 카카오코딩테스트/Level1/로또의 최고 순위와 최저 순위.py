def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
        elif i == 0:
            zero += 1
    best = cnt + zero
    if best == 0:
        answer.append(6)
    else:
        answer.append(7-best)
    if cnt == 0:
        answer.append(6)
    else:
        answer.append(7-cnt)
    return answer


# 정답 예시 코드
# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]