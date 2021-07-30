from random import randint #랜덤 함수에서 randint만 가져옴

#숫자 3개를 뽑아주는 generate_numbers 함수 작성하기
def generate_numbers():
    numbers = [] #랜덤으로 3개의 숫자를 담은 리스트

    while len(numbers) < 3: #숫자 3개를 뽑기 위해 리스트의 길이를 이용해 조건문 만듦
        num = randint(0, 9) #0 ~ 9 사이의 숫자를 랜덤으로 하나 뽑음
        if num not in numbers: #중복된 수를 뽑으면 안되기 때문에 뽑은 숫자가 리스트에 없을 경우에만 리스트에 추가해줌
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers #함수의 반환값은 뽑은 세개의 숫자여야 하므로 numbers 리스트를 반환해줌

#유저에게 숫자 3개를 입력받는 take_guess 함수 작성하기
#take_guess 함수는 결과적으로 리스트를 리턴해야 함
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = [] #3개의 숫자를 입력 받아 저장하는 리스트

    while len(new_guess) < 3: #숫자를 3개만 입력 받아야 하므로 리스트의 길이를 제한하므로써 조건을 만듦
        new_num = int(input("{}번째 숫자를 입력하세요:".format(len(new_guess) + 1))) #입력 받는 숫자(리스트의 길이를 이용해 몇번째 숫자인지 표시해줌)

        if new_num < 0 or new_num > 9: #숫자가 0 ~ 9 사이에 있지 않으면 오류, 다시 실행
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess: #숫자가 중복되는 수이면 오류, 다시 실행
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else: #알맞은 수 이면 new_guess 리스트에 추가
            new_guess.append(new_num)

    return new_guess #함수의 반환값은 유저가 입력한 세개의 숫자여야 하므로 new_guess 리스트를 반환해줌

#스트라이크 수와 볼 수를 알려주는 get_score 함수 작성하기
def get_score(guess, solution): #guess, solution 2개의 파라미터를 받음
    strike_count = 0 #스트라이크 개수
    ball_count = 0 #볼 개수

    for i in range(3): #리스트 내 숫자가 3개이므로, 입력한 숫자들과 정답 리스트 숫자들을 서로 비교하기 위해 range 범위를 3으로 설정, for문 실행
        #s판단
        if guess[i] == solution[i]: #guess와 solution에서 리스트 내에 같은 위치에 같은 숫자가 있으면 스트라이크
            strike_count += 1
        #b판단
        if guess[i] in solution and guess[i] != solution[i]: #guess의 숫자가 solution 리스트 내에 존재하지만, 리스트 내에서 다른 위치에 있을때 볼
            ball_count += 1

    return strike_count, ball_count #스트라이크와 볼의 개수를 반환

#여기서부터 게임 시작

ANSWER = generate_numbers() #3개 숫자를 맞추는 프로그램이므로, 3개의 숫자를 ANSWER로 먼저 뽑아줌
tries = 0 #시도 횟수를 카운트 하기 위한 변수

while True:
    user_guess = take_guess() #유저의 숫자 3개를 뽑음
    s, b = get_score(user_guess, ANSWER) #뽑은 숫자와 정답을 비교하기 위해 get_score 함수의 파라미터로 user_guess와 ANSWER를 받음

    print("{}S {}B\n".format(s, b)) #get_score 함수를 통해 얻은 스트라이크 수와 볼 수를 출력
    tries += 1

    if s == 3: #스트라이크가 3개이면 정답을 모두 맞춘 것이므로 while문 탈출
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
print("의미있는 그런 숫자야구라고 생각합니다!! 싸인")