import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def multi (a,n):
  if n == 1:
      return A % C
  else:
      tmp = multi(a, n // 2)
      if n % 2 == 0:
          return (tmp * tmp) % C
      else:
          return (tmp * tmp * A) % C
          
print(multi(A, B))