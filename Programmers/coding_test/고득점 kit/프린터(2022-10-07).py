from collections import deque

def solution(priorities, location):
    index_list = deque([i for i in range(len(priorities))])
    print_order = 0
    while index_list:
        front = index_list.popleft()
        check_list = [ index for index in index_list if priorities[front] < priorities[index]]

        # 존재하지 않아
        if not check_list:
            print_order += 1
            if front == location:
                return print_order
        else:
            index_list.append(front)
            
'''
# 다른사람의 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
'''