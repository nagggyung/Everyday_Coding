def solution(x):
    answer = 0
    cur, next = 0,1 
    
    # x 가 1인 경우 
    if x == 1:
        return 1
    
    # x 가 2 이상인 경우 
    else:
        for n in range(x+1):
            if n >= 2:
                answer = cur + next 
                cur = next 
                next = answer 
    return answer      
            