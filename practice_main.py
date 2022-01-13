def solution(n, arr1, arr2):

    wall = []
    for i in range(n):
        arr1[i] = int(bin(arr1[i])[2:])
        arr2[i] = int(bin(arr2[i])[2:])
        wall.append(str(arr1[i] + arr2[i]))
    for i in range(n):
        wall[i] = wall[i].replace('1','#')
    print(wall)
solution(5,	[9, 20, 28, 18, 11], [30, 1, 21, 17, 28])