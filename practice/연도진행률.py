today = list(input("입력예시 : May 6, 1997 16:18\n").split())
month = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31\
    , 'September':30, 'October':31, 'November':30, 'December':31}
alltime = 525600
if int(today[2]) % 400 == 0 or (int(today[2]) % 4 == 0 and int(today[2]) % 100 != 0):
    month['February'] = 29
    alltime = 527040
time = (sum(list(month.values())[:list(month.keys()).index(today[0])])\
     + (int(today[1][:2]) - 1)) * 1440 + (int(today[3][:2]) * 60) + int(today[3][3:])
print((time / alltime) * 100)