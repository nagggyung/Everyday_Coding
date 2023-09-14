from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        price = prices.popleft()
        sec = 0
        for n in prices:
            sec += 1
            if price > n:
                break
        answer.append(sec)
    return answer

'''
# 다른 사람의 풀이
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]:
                past, _ = stack.pop()
                answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
'''