import sys

N = int(input())
num_1 = list(map(int, sys.stdin.readline().rsplit()))
M = int(input())
num_2 = list(map(int, sys.stdin.readline().rsplit()))

for i in range(M):
    if num_2[i] in num_1:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')