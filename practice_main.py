import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

block1_1 = [(0, 0), (0, 1), (0, 2), (0, 3)]
block1_2 = [(0, 0), (1, 0), (2, 0), (3, 0)]
block2 = [(0, 0), (1, 0), (0, 1), (1, 1)]
block3_1 = [(0, 0), (1, 0), (2, 0), (2, 1)]
block3_2 = [(0, 1), (1, 1), (1, 2), (0, 2)]
block3_3 = [(0, 0), (0, 1), (1, 0), (2, 0)]
block3_4 = [(0, 0), (0, 1), (1, 1), (2, 1)]
block4_1 = [(0, 0), (1, 0), (1, 1), (2, 1)]
block4_2 = [(0, 1), (1, 1), (1, 0), (2, 0)]
block5_1 = [(0, 0), (0, 1), (0, 2), (1, 1)]
block5_2 = [(0, 1), (1, 1), (1, 0), (2, 1)]
block5_3 = [(0, 1), (1, 0), (1, 1), (1, 2)]
block5_4 = [(0, 0), (1, 0), (2, 0), (1, 1)]

block_set = (block1_1, block1_2, block2, block3_1, block3_2, block3_3, block3_4, block4_1, block4_2, 
             block5_1, block5_2, block5_3, block5_4)

for block in block_set:
    total = board[block[0][0]][block[0][1]] + board[block[1][0]][block[1][1]] + board[block[2][0]][block[2][1]] + board[block[3][0]][block[3][1]]
    while True:
        while True:
            for point in block:
                if point[1] + 1 == M:
                    break
                point[1] += 1