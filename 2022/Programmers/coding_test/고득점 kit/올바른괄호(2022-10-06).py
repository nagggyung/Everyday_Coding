def solution(s):
    hash_map={
        ')':'('
    }
    answer = True
    stack = []

    for a in s:
        if a == '(':
            stack.append(a)
            continue
        if a == ')':
            if not stack:
                answer = False
                break
            else:
                if stack.pop() == hash_map[a]:
                    continue
                else:
                    answer = False
                    break
    if stack:
        answer = False
    return answer

'''
# 다른 사람의 풀이
def is_pair(s):
    # 함수를 완성하세요
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0
'''