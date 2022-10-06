def solution(progresses, speeds):
    answer = []
    left = []
    
    for i, prog in enumerate(progresses):
        item = (100-prog)//speeds[i] if (100-prog)%speeds[i] == 0 else (100-prog)//speeds[i]+1
        left.append(item)
    left.reverse()
    while left:
        day = left.pop()
        count = 1
        while len(left) != 0 and day >= left[-1]:
            left.pop()
            count += 1
        answer.append(count)
    return answer        

'''
# 다른사람의 풀이

from math import ceil

def solution(progresses, speeds):
    daysLeft = list(map(lambda x: (ceil((100 - progresses[x]) / speeds[x])), range(len(progresses))))
    count = 1
    retList = []

    for i in range(len(daysLeft)):
        try:
            if daysLeft[i] < daysLeft[i + 1]:
                retList.append(count)
                count = 1
            else:
                daysLeft[i + 1] = daysLeft[i]
                count += 1
        except IndexError:
            retList.append(count)

    return retList
'''