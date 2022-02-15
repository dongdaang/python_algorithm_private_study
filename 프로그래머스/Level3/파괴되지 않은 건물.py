def solution(board, skill):
    answer = 0
    for info in skill:
        for i in range(info[1], info[3]+1):
            for j in range(info[2], info[4]+1):
                if info[0] == 1:
                    board[i][j] -= info[5]
                else:
                    board[i][j] += info[5]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer

#다른 풀이(누적 합 활용)
# def solution(board, skill):
#     answer = 0
#     for info in skill:
#         cnt = 0
#         skill_board = [[0 for _ in range(info[4]+2)] for _ in range(info[3]+2)]
#         skill_board[info[1]][info[2]] = skill_board[info[3]+1][info[4]+1] = info[5]
#         skill_board[info[1]][info[4]+1] = skill_board[info[3]+1][info[2]] = -info[5]
#         for i in range(info[1], info[3]+2):
#             for j in range(info[2], info[4]+1):
#                 skill_board[i][j+1] += skill_board[i][j]
#         for j in range(info[2], info[4]+2):
#             for i in range(info[1], info[3]+1):
#                 skill_board[i+1][j] += skill_board[i][j]
#         for i in range(info[1], info[3]+1):
#             for j in range(info[2], info[4]+1):
#                 if info[0] == 1:
#                     board[i][j] -= skill_board[i][j]
#                 else:
#                     board[i][j] += skill_board[i][j]
#     for i in board:
#         for j in range(len(i)):
#             if i[j] > 0:
#                 answer += 1
    
#     return answer