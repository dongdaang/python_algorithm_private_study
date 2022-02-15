def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for i in reserve[:]:
        if i in lost[:]:
            reserve.remove(i)
            lost.remove(i)
    for i in reserve[:]:
        for j in lost[:]:
            if i - 1 == j or i + 1 == j:
                lost.remove(j)
                reserve.remove(i)
                break
    answer = n - len(lost)
    return answer

##############또 다른 풀이##############

# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)
