import copy

a = [[1,2], [3,4]]
b = copy.deepcopy(a)
# b = [a[i] for i in range(len(a[0]))]
b[0][1] = 1212
print(b)
print(a)