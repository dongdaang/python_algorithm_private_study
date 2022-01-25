def solution(id_list, report, k):
    answer = []
    a = {}
    cnt = {}
    result = {}
    for name in id_list:
        result[name] = 0
    for info in report:
        info = info.split(' ')
        if info[0] not in a:
            a[info[0]] = [info[1]]
        elif info[1] not in a[info[0]]:
            a[info[0]].append(info[1])
    for v in a.values():
        for name in v:
            if name not in cnt:
                cnt[name] = 1
            else:
                cnt[name] += 1
    for key, value in cnt.items():
        if value >= k:
            for i, j in a.items():
                if key in j:
                    result[i] += 1
    for v in result.values():
        answer.append(v)
    return answer

# 정답 예시 코드

# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer