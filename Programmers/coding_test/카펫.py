def solution(brown, yellow):
    num = brown+yellow
    res=[]
    for w in range(4,num):
        for h in range(3,num):
            if num%w == 0 and num == w*h:
                print(w)
                print(h)
    
            
    return res