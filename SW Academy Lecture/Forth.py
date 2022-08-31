T = int(input())

for test_case in range(1, T + 1):
    cal_string = input()
    cal_list = cal_string.split(' ')
    stack = []

    try:
        for token in cal_list[0:len(cal_list)-1]:
            if token.isdigit():
                stack.append(token)
                continue
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if token == '+':
                    c = b+a
                    stack.append(c)
                    continue
                elif token == '-':
                    c = b-a
                    stack.append(c)
                    continue
                elif token == '*':
                    c = b*a
                    stack.append(c)
                    continue
                elif token == '/':
                    if not a or not b:
                        stack.append(0)
                    else:
                        c = b//a
                        stack.append(c)
                    continue
        res = stack.pop()
        if stack:
            print(f'#{test_case} error')
        else:
            print(f'#{test_case} {res}')
    except:
        print(f'#{test_case} error')
 