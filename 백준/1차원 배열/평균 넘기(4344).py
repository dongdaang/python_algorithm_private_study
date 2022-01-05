import sys

input = sys.stdin.readline

C = int(input())
students = []
result = []
for _ in range(C):
    score = list(map(int, input().split()))
    cnt = 0
    N = score[0]
    avg = (sum(score) - score[0]) / N
    for i in range(1, N+1):
        if score[i] > avg:
            cnt += 1
    value = ((cnt / score[0]) * 100)
    result.append(value)
for i in result:
    print("{:.3f}%".format(i))

# 정답코드 예시
# n = int(input())

# for _ in range(n):
#     nums = list(map(int, input().split()))
#     avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
#     cnt = 0
#     for score in nums[1:]:
#         if score > avg:
#             cnt += 1  # 평균 이상인 학생 수
#     rate = cnt/nums[0] *100
#     print(f'{rate:.3f}%')