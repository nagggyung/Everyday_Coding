import heapq
def solution(scoville, K):
    heapq.heapify(scoville) 
    count = 0
    while scoville:
        s = heapq.heappop(scoville)
        if s < K:
            if len(scoville) == 0:
                return -1
            heapq.heappush(scoville, s+heapq.heappop(scoville)*2)
            count += 1
        else:
            return count 


            
            
    