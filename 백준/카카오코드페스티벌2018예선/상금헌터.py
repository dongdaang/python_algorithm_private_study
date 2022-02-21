import sys
input = sys.stdin.readline

T = int(input())
scores = []
result = []
for _ in range(T):
    scores.append(list(map(int, input().split())))

contest1 = {500:[1], 300:[i for i in range(2, 4)], 200:[i for i in range(4, 7)], 50:[i for i in range(7, 11)], 30:[i for i in range(11, 16)], 10:[i for i in range(16, 22)]}
contest2 = {512:[1], 256:[i for i in range(2, 4)], 128:[i for i in range(4, 8)], 64:[i for i in range(8, 16)], 32:[i for i in range(16, 32)]}

for score in scores:
    prize = 0
    for k, v in contest1.items():
        if score[0] in v:
            prize += k
    for k, v in contest2.items():
        if score[1] in v:
            prize += k
    result.append(prize * 10000)
    
for i in result:
    print(i)