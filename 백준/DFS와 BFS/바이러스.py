import sys

input = sys.stdin.readline

def virus():
    
n = int(input().rstrip())
m = int(input().rstrip())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1