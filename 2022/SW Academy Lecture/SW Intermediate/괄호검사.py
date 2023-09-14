

def check_match(words):
    dic = {'}': '{', ')': '('}
    stack = []
    for w in words:
        if w == '{' or w =='(':
            stack.append(w)
        if w == '}' or w ==')':
            if not stack:
                return 0
            if dic[w] != stack[-1]:
                return 0
            stack.pop()
    if stack:
        return 0
    return 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    words = input()
    print(f'#{test_case} {check_match(words)}')


