train_list = []             #모든 열차 리스트
reservation_list = []       #나의 예매 현황 리스트
departure_list = []         #가능한 출발역 리스트
arrival_list = []           #가능한 도착역 리스트
train_type_list = []        #가능한 열차종류 리스트

with open('TrainList.txt', 'r') as file:                    #7 ~ 10 : 텍스트 파일로 된 열차 리스트 불러오기
    for text in file:
        train_list.append(text.strip().split(' '))
        print(text.strip('\n'))
for i in range(1, len(train_list)):                         #11 ~ 18 : 열차 리스트에서 출발역으로 가능한 위치는 departure_list,
    train_list[i][0] = train_list[i][0].replace(':','')     #          도착역으로 가능한 위치는 arrival_list,
    if train_list[i][1] not in departure_list:              #          열차종류로 가능한 것은 train_type_list에 저장
        departure_list.append(train_list[i][1])
    if train_list[i][3] not in arrival_list:
        arrival_list.append(train_list[i][3])
    if train_list[i][4] not in train_type_list:
        train_type_list.append(train_list[i][4])
    
class my_train:
    def __init__(self):     #객체 생성 시에 입력은 받지 않음
        pass

    def reservation(self):          #열차 예약 함수
        while True:
            try:
                self.time = int((input('원하는 시간(입력예시: 08:35 -> 0835) : ')))         #25 ~ 37 : 시간 입력 받기
                if self.time > int(train_list[-1][0]):
                    print("해당 시간 이후에 출발하는 열차는 없습니다.")
                    continue
                elif self.time % 100 >= 60:
                    print("올바른 입력이 아닙니다.")
                    continue
            except ValueError:
                print("옳바른 입력이 아닙니다.")
                continue
            break
        while True:                                         #38 ~ 43 : 출발역 입력 받기
            self.departure = input('출발역 : ')
            if self.departure not in departure_list:
                print("해당 역은 존재하지 않습니다.")
            else:
                break
        while True:                                         #44 ~ 49: 도착역 입력 받기
            self.arrival = input('도착역 : ')
            if self.arrival not in arrival_list:
                print("해당 역은 존재하지 않습니다.")
            else:
                break
        while True:                                         #50 ~ 55 : 열차종류 입력 받기
            self.train_type = input('열차종류 : ')
            if self.train_type not in train_type_list:
                print("해당 열차는 존재하지 않습니다.")
            else:
                break
        for i in range(1, len(train_list)):
            if self.time <= int(train_list[i][0]) and train_list[i][1] == self.departure and train_list[i][3] == self.arrival\
                and train_list[i][4] == self.train_type and train_list[i][5] != '매진':
                print("예매 가능한 열차 : {0}:{1} {2} {3} {4} {5}   잔여 좌석 수 : {6}".format(train_list[i][0][0:2],\
                    train_list[i][0][2:], train_list[i][1], train_list[i][2], train_list[i][3], train_list[i][4], train_list[i][5]))
                while True:
                    num = input("해당 열차를 예매하시겠습니까?   1. 예매   (돌아가기는 아무 키나 누르시오)\n")
                    if num == str(1):
                        train_list[i][5] = int(train_list[i][5]) - 1            #56 ~ 72 : 입력한 정보와 비교했을 때 가능한 열차가 있는 경우
                        reservation_list.append(train_list[i])                  #          예매를 진행함, 동시에 예매가 끝난 후 남은 좌석이
                        print("예매가 완료되었습니다.")                          #          0인 경우 매진으로 표시해줌
                        if train_list[i][5] == 0:
                            train_list[i][5] = '매진'
                        break
                    else:
                        break
                break
            elif self.time <= int(train_list[i][0]) and train_list[i][1] == self.departure and train_list[i][3] == self.arrival\
                and train_list[i][4] == self.train_type and train_list[i][5] == '매진':
                print("해당 열차는 매진입니다.")            #73 ~ 76 : 입력한 정보가 매진이 되었을 경우 매진이라고 표시
                break

    def all_train(self):                    #78 ~ 82 : 전체 열차 리스트를 보여주는 함수
        print("\n")
        for i in range(1, len(train_list)):
            print("{0}:{1} {2} {3} {4} {5}   잔여 좌석 수 : {6}".format(train_list[i][0][0:2], train_list[i][0][2:],\
                train_list[i][1], train_list[i][2], train_list[i][3], train_list[i][4], train_list[i][5]))
    
    def my_infomation(self):                #84 ~ 90 : 나의 예매 현황을 보여주는 함수
        print("\n나의 예매 내역")
        if len(reservation_list) == 0:
            print("예매 내역이 없습니다.")
        else:
            for i in reservation_list:
                print("{0}:{1} {2} {3} {4} {5}".format(i[0][0:2], i[0][2:], i[1], i[2], i[3], i[4]))

    def reservation_cancel(self):           #92 ~ 122 : 예매 내역 취소 함수
        while True:
            if len(reservation_list) != 0:
                print("\n나의 예매 현황")
                for i in range(len(reservation_list)):
                    print("{0} : {1}:{2} {3} {4} {5} {6}".format(i+1, reservation_list[i][0][0:2], reservation_list[i][0][2:],\
                        reservation_list[i][1], reservation_list[i][2], reservation_list[i][3], reservation_list[i][4]))
                try:
                    num = int(input("\n어떤 예매내역을 취소하시겠습니까?(번호로 입력, 뒤로가기 : 0)"))
                    if num in range(1, len(reservation_list)+1):
                        for j in range(1, len(train_list)):
                            if reservation_list[num-1][0:5] == train_list[j][0:5]:   #예매 현황을 reservation_list에 저장된 정보를 통해 한번에 볼 수 있음
                                del(reservation_list[num-1])                         #매진이던 열차가 예매 취소 되는 경우 좌석을 1로 바꿔줌
                                if train_list[j][5] == '매진':                       #예매를 취소할 경우 reservation_list에서 해당 내역 삭제
                                    train_list[j][5] = 1                             #예매 내역이 없는 경우 내역 없음 표시 후 종료
                                    train_list[j][5] = int(train_list[j][5])           
                                else:                                                                    
                                    train_list[j][5] += 1
                                print("\n예매가 취소되었습니다.")
                                break
                        break
                    elif num == 0:
                        break
                    else:
                        print("\n잘못된 번호입니다.")
                except ValueError:
                    print("옳바른 입력이 아닙니다.")
                    continue
            else:
                print("예매 내역이 없습니다.")
                break
        
user = my_train()

while True:
    print("\n기차예매 프로그램\n\n1. 빠른시간 기차 검색 및 예매\n2. 전체기차 리스트\n3. 나의 예매 현황\n4. 예매 취소\n5. 프로그램 종료")
    menu = int(input("\n메뉴 선택 : "))

    if menu == 1:
        user.reservation()
    elif menu == 2:
        user.all_train()
    elif menu == 3:
        user.my_infomation()
    elif menu == 4:
        user.reservation_cancel()
    elif menu == 5:
        break

print("\n프로그램이 종료되었습니다.")