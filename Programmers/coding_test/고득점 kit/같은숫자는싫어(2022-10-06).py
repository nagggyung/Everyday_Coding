def solution(arr):
    stack = []
    for num in arr:
        if not stack:
            stack.append(num)
            continue
        if stack[-1] == num:
            continue
        stack.append(num)
    return stack
    
    
    '''
    # 다른 사람의 풀이
    
    def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
    
    '''