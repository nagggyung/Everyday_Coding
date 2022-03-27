def solution(answers):
    first = [1,2,3,4,5]*10000
    second = [2,1,2,3,2,4,2,5]*10000
    third = [3,3,1,1,2,2,4,4,5,5]*10000
    
    score = [0,0,0]
    answer = []
    
    for i in range(len(answers)):
        if first[i] == answers[i]:
            score[0] += 1
            
        if second[i] == answers[i]:
            score[1] += 1
            
        if third[i] == answers[i]:
            score[2] += 1

    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i+1)
    
    return answer