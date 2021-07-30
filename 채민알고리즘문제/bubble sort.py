A = list(map(int, input()))
for i in range(0, len(A)):
    for j in range(i+1, len(A)):
        if A[i] > A[j]:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    print(A[i], end = '')