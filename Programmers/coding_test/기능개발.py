import math

def solution(progresses, speeds):
    days = []
    res = []
    
    for i in range(len(progresses)):
        a = math.ceil((100-progresses[i])/speeds[i])
        days.append(a)
    
    days.reverse()
    
    #[9,3,7]
    
    while days:
        day_right = days.pop() #7
        count = 1
        while len(days) != 0 and day_right >= days[-1]:
            count += 1
            days.pop()
        res.append(count)
        
    return res