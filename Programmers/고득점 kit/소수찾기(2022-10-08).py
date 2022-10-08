from itertools import permutations
def solution(numbers):
    res = []
    answer = 0
    numbers = list(numbers)
    
    # 1. 숫자 조합 만들기
    for i in range(1, len(numbers)+1):
        items = permutations(numbers, i)
        for item in items:
            item = "".join(item)
            if int(str(item)) not in res:
                res.append(int(str(item)))
            else:
                continue
    
    # 2. 소수 판단
     
    for num in res:
        if num == 0 or num == 1:
            continue
        check = True # 소수다
        for s in range(2,int((num**0.5)+1)): # 2~루트 num 까지 나누어지는지 확인 !  
            if num%s == 0:
                check = False
                break
        if check:
            answer+=1
            

    return answer