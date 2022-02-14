def solution(n, lost, reserve):
    answer = 0
    tmp = lost.copy()
    for i in tmp:
        if i - 1 in reserve:
            lost.remove(i)
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            lost.remove(i)
            reserve.remove(i + 1)
    answer = n - len(lost)
    return answer

print(solution(5, [2, 4], [1, 3, 5]))