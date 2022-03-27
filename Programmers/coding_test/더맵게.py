import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < K:
        if len(scoville)> 1:
            smallest = heapq.heappop(scoville)
            second_smallest = heapq.heappop(scoville)

            cal = smallest+second_smallest * 2
            heapq.heappush(scoville, cal)
            answer += 1
        else:
            return -1
    
    return answer
        
        
        
    
