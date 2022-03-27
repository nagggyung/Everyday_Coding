import heapq

def solution(operations):
    minh, maxh = [], []
    
    for operation in operations:
        op, data = operation.split()

        if op == 'I':
            heapq.heappush(minh, int(data))
            heapq.heappush(maxh, -int(data))
        
        if op == 'D':
            # 빈 큐에 삭제 연산 시 무시 
            if len(minh) == 0 or len(maxh)==0:
                continue
            if data == '-1':
                minh_value = heapq.heappop(minh)
                maxh.remove(-minh_value)
                
            if data == '1':
                maxh_value = heapq.heappop(maxh)
                minh.remove(-maxh_value)
            
    if not minh and not maxh:
        return [0,0]
    else:
        max_value = heapq.heappop(maxh)
        min_value = heapq.heappop(minh)
        
        return [-max_value, min_value]