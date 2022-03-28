import sys
input = sys.stdin.readline

N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

res1 = ''
res2 = ''
res3 = ''
def first(root):
    global res1
    if root != '.':
        res1 += root
        first(tree[root][0])
        first(tree[root][1])

def mid(root):
    global res2
    if root != '.':
        mid(tree[root][0])
        res2 += root
        mid(tree[root][1])

def last(root):
    global res3
    if root != '.':
        last(tree[root][0])
        last(tree[root][1])
        res3 += root
        
first('A')
mid('A')
last('A')

print(res1)
print(res2)
print(res3)