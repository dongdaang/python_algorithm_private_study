a = [1,2,3]
a.append(0)
for i in range(len(a)):
    a[i+1] = a[i]
a[0] = 0    
print(a)