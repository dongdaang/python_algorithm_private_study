def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    a = []
    b = []
    for i in range(len(str1)-1):
        if (str1[i]+str1[i+1]).isalpha():
            a.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if (str2[i]+str2[i+1]).isalpha():
            b.append(str2[i]+str2[i+1])
    c = []
    d = []
    for i in b:
        if i in a:
            c.append(i)
            a.remove(i)
    d = a + b
    if d == []:
        answer = 65536
    else:
        answer = int((len(c) / len(d)) * 65536)

    return answer

# 정답 예시 코드

# import re
# import math

# def solution(str1, str2):
#     str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
#     str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

#     gyo = set(str1) & set(str2)
#     hap = set(str1) | set(str2)

#     if len(hap) == 0 :
#         return 65536

#     gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
#     hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

#     return math.floor((gyo_sum/hap_sum)*65536)