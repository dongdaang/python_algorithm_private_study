import sys

input = sys.stdin.readline

def virus(a):
    for i in range(1, n + 1):
        if graph[a][i] == 1 and virus_list[i] == 0:
            virus_list[i] = 1
            virus(i)

n = int(input().rstrip())
m = int(input().rstrip())
graph = [[0] * (n + 1) for _ in range(n + 1)]
virus_list = [0] * (n + 1)
virus_list[1] = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

virus(1)
print(virus_list.count(1) - 1)