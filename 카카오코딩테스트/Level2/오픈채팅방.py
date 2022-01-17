# def solution(record):
#     answer = []
#     name = {}
#     for i in record:
#         tmp = i.split(' ')
#         if tmp[0] != 'Leave':
#             name[tmp[1]] = tmp[2]
#     for i in record:
#         tmp = i.split(' ')
#         if tmp[1] in name:
#             if tmp[0] == 'Enter':
#                 answer.append(name[tmp[1]]+'님이 들어왔습니다.')
#             elif tmp[0] == 'Leave':
#                 answer.append(name[tmp[1]]+'님이 나갔습니다.')
#     return answer



# 정답 예시 1

# def solution(record):
#     answer = []
#     namespace = {}
#     printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
#     for r in record:
#         rr = r.split(' ')
#         if rr[0] in ['Enter', 'Change']:
#             namespace[rr[1]] = rr[2]

#     for r in record:
#         if r.split(' ')[0] != 'Change':
#             answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

#     return answer

# 정답 예시 2
# def solution(record):
#     user_id = {EC.split()[1]:EC.split()[-1] for EC in record if EC.startswith('Enter') or EC.startswith('Change')}
#     return [f'{user_id[E_L.split()[1]]}님이 들어왔습니다.' if E_L.startswith('Enter') else f'{user_id[E_L.split()[1]]}님이 나갔습니다.' for E_L in record if not E_L.startswith('Change')]