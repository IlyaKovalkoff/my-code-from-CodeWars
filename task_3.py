


def solution(text):
    list = []
    step = ''
    count = 0
    for i in text:
        step += i
        count += 1
        if count > 1:
            count = 0
            list.append(step)
            step = ''
    if len(list) < (len(text) / 2):
        list.append(i + '_')    
    return list
print (solution('hello worldd'))