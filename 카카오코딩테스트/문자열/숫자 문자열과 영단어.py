def solution(s):
    answer = ''
    num = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    while(True):
        tmp = ''
        for i in range(len(s)):
                tmp += s[i]
                if tmp in num.keys():
                    answer += num[tmp]
                    tmp = ''
                elif s[i].isdigit():
                    answer += tmp
                    tmp = ''
        break
    return int(answer)
solution('one4seveneight')


# 정답코드 예시
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)