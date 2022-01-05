N = int(input())
num = 1
end_num_list = []
end_num = '666'
while len(end_num_list) <= 10000:
    if end_num in str(num):
        end_num_list.append(num)
    num += 1
print(end_num_list[N-1])