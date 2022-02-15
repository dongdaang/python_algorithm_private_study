def solution(board, moves):
    answer = 0
    bucket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                bucket.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(bucket) >= 2:
            if bucket[-1] == bucket[-2]:
                bucket.pop()
                bucket.pop()
                answer += 2
    return answer