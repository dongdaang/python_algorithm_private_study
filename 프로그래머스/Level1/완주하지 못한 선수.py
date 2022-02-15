from collections import Counter

def solution(participant, completion):
    answer = ''
    name = Counter(participant)
    for person in completion:
        name[person] -= 1
    for k, v in name.items():
        if v != 0:
            answer = k
    return answer

##########또 다른 풀이##########
# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]