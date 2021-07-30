import random
import sys

num1, num2, num3, num4, num5, num6 = map(int, input("1~45 사이의 숫자 6개를 입력해주시오: ").split())

my_num = []
cnt = 0
price = 6
bonus_cnt = 0

my_num.append(num1)
my_num.append(num2)
my_num.append(num3)
my_num.append(num4)
my_num.append(num5)
my_num.append(num6)

my_num.sort()

for i in range(7):
    val = random.sample(range(1,45),7)

bonus = val[6]
val = val[0:6]

for i in my_num:
    if i > 45 or i < 1:
        print("알맞은 번호가 아닙니다.")
        exit()
    else:
        for j in val:
            if i == j:
                cnt += 1

for i in my_num:
    if i == bonus:
        bonus_cnt = 1

if cnt == 6:
    price == 1
if cnt == 5 and bonus_cnt == 1:
    price == 2
if cnt == 5 and bonus_cnt == 0:
    price == 3
if cnt == 4:
    price == 4
if cnt == 3:
    price == 5

print("내 번호 : {0}".format(my_num))
print("추첨 번호 : {0} 보너스 : {1}".format(val, bonus))
print("맞은 개수 : {0} + {1}".format(cnt, bonus_cnt))
print("등수 : {0}".format(price))