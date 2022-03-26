import collections

def solution(priorities, location):
    max_value = max(priorities)
    indexes = collections.deque([i for i in range(len(priorities))])
    answer = 0 # 인쇄 횟수
    max_index = priorities.index(max_value)
    
    while True:
        index = indexes.popleft()
        if priorities[index] < max_value:
            indexes.append(index)
        else:
            answer += 1 
            priorities[index] = 0
            
            # 인쇄 후 남은 우선 순위 중 max_value 찾는다.
            max_value = max(priorities)
            
            # location 값인 경우 인쇄 횟수 인 answer return 
            if location == index:
                return answer
            