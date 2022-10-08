# 문제 제한 조건을 잘보자..


def solution(answers):
    count = [0,0,0]
    p_1 = [1,2,3,4,5]*10000
    p_2 = [2,1,2,3,2,4,2,5]*10000
    p_3 = [3,3,1,1,2,2,4,4,5,5]*10000
    answer = []
    
    for i in range(len(answers)):
        if answers[i] == p_1[i]:
            count[0]+=1
        if answers[i] == p_2[i]:
            count[1]+=1
        if answers[i] == p_3[i]:
            count[2]+=1
    
    max_res = max(count)
    for i in range(len(count)):
        if max_res == count[i]:
            answer.append(i+1)
    return sorted(answer)
            