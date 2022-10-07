def solution(operations):
    answer = []
    queue = []
    
    for command in operations:
        c1, c2 = command.split()
        if c1 == 'I':
            queue.append(int(c2))
            continue
        if c1 == 'D':
            if c2 == '-1':
                if queue:
                    queue.remove(min(queue))
                    continue
            else:
                if queue:
                    queue.remove(max(queue))
                    continue
    if queue:
        answer.extend([max(queue), min(queue)])
    else:
        answer.extend([0,0])
    return answer