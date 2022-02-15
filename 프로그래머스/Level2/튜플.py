def solution(s):
    answer = []
    tmp = []
    m = 0
    result = 0
    s = s.split('},{')
    s[0] = s[0][2:]
    s[-1] = s[-1][:-2]
    s.sort(key=lambda x: len(x))
    for i in s:
        i = i.split(',')
        i = list(map(int, i))
        tmp.append(i)
    for i in tmp:
        for j in range(len(i)):
            if i[j] not in answer:
                answer.append(i[j])
    return answer


# 정답 예시 코드
# def solution(s):

#     s = Counter(re.findall('\d+', s))   특정 문자 개수 세어주는 Counter함수
#     return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

# import re
# from collections import Counter