#내풀이: 정확성테스트 통과, 효율성 테스트 통과 x

import collections
def solution(gems):
    temp_ans = []
    # 1. 종류/갯수 확인
    gems_set = set(gems)
    gems_count = len(gems_set)
    
    #2. start, end 초기화
    start, end = 0, 0
    while start <= end and end < len(gems):
        # 모든 종류를 다 가지고 있는 경우 
        if len(set(gems[start:end+1])) == gems_count:
            temp_ans.append([start+1,end+1,end-start])
            start += 1
        elif gems[start] == gems[end] and end != 0:
            start += 1
        else: end += 1

    temp_ans.sort(key=lambda x:(x[2],x[0]))
    return temp_ans[0][:2]      
            
   # 정답코드
   # 딕셔너리 이용해서 문제 품
   
import collections
def solution(gems):
    answer = [0, 0]
    l = len(set(gems))
    contained = {}
    shortest = len(gems)+1
    left, right = 0, 0
    
    while right < len(gems):
        if gems[right] not in contained:
            contained[gems[right]] = 1
        else:
            contained[gems[right]] += 1
        
        if len(contained) == l:
            while left <= right:
                if contained[gems[left]] > 1:
                    contained[gems[left]] -= 1
                    left += 1
                elif (right-left) < shortest:
                    shortest = right-left
                    answer = [left+1, right+1]
                    del contained[gems[left]]
                    left += 1
                    break
                else:
                    break
        right += 1
    return answer
                    
        
        