# from collections import deque

# def solution(progresses, speeds):
#     answer = []
#     tmp = 0
#     deq = deque()
#     a = 1
#     for i in range(len(progresses)):
#         while(progresses[i] < 100):
#             progresses[i] += speeds[i]
#             tmp += 1
#         deq.append(tmp)
#         tmp = 0
#     if len(deq) == 1:
#         answer.append(a)
#     else:
#         while(len(deq) >= 2):
#             if deq[0] < deq[1]:
#                 answer.append(a)
#                 a = 1
#                 deq.popleft()
#             else:
#                 a += 1
#                 deq.popleft()
#         answer.append(a)
#     print(answer)
#     return answer

# solution([93, 30, 55], [1, 30, 5])

#정답코드 예시
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
solution([93, 30, 55], [1, 30, 5])