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
            
   '''
   투포인터 알고리즘

   


   '''
