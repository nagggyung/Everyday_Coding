def check_match(str):
    dict_form = {']': '[', ')': '(', '}': '{'}
    stack = []

    for w in string:
        if w in list(dict_form.values()):
            stack.append(w)
            continue
        if w in list(dict_form.keys()):
            if not stack: # 스택이 빈 값인 경우(비교 값 존재x)
                return 0
            if dict_form[w] != stack.pop(): # 괄호 짝이 안맞는 경우
                return 0
    if stack:  # 문자열을 다 돌았음에도 stack에 괄호가 남아있는 경우(괄호 짝 안맞음)
        return 0
    return 1

T = int(input())
for test_case in range(1, T + 1):
    string = input()
    print(f'#{test_case} {check_match(string)}')







