# 개인적으로 아이디어 생각해 내기 어려웠던 문제..
# 유튜브 참고해서 풀었다..


import heapq
from collections import deque
# 힙에다가 튜플(tuple)를 원소로 추가하거나 삭제하면, 
#튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리
def solution(jobs):
    jobs.sort()
    heap_list = []
    count, last = 0, -1 # pop count, 시작 점 
    length = len(jobs)
    total = 0
    time = jobs[0][0]
    while count < length:
        for t, l in jobs:
            if last < t <= time:
                heapq.heappush(heap_list, (l,t))
        if heap_list:
            l, t = heapq.heappop(heap_list)
            count += 1
            last = time
            time += l
            total += (time - t)
        else:
            time += 1
    return total//length

'''
# 다른사람 풀이..

import heapq
from collections import deque

def solution(jobs):
    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)
'''
            
        