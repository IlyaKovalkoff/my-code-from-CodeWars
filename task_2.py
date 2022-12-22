def FirstReverse(strParam):
    lens = len(strParam) - 1
    answer = ''
    while lens >= 0:
        answer += strParam[lens]
        lens -= 1

  # code goes here
    return answer



print(FirstReverse('Hello World'))