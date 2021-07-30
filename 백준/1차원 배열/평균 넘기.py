C = int(input())

percent = []

for i in range(C):
    score = list(map(int, input().split()))
    cnt = 0
    sum = 0
    N = score[0]
    if N >= 1 and N <= 1000:
        for i in range(1,N+1):
            sum += score[i]
        avg = float(sum / N)
        for i in range(1,N+1):
            if score[i] > avg:
                cnt += 1
        over_avg = float(cnt / N) * 100
        percent.append(over_avg)
for i in percent:
    print("{:.3f}%".format(i))