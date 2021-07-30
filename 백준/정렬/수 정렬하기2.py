a = []
N = int(input())
for i in range(N):
    num = int(input())
    a.append(num)
a.sort()
for i in range(len(a)):
    print(a[i])

# import sys

# N = int(input())
# arr = [int(sys.stdin.readline()) for _ in range(N)]
# sys.stdout.write("\n".join(map(str, sorted(arr))))        #참고 : 수를 여러줄 입력 받을 때
                                                            #       input()보다 sys.stdin.readline()이 더 빠름