T = int(input())
for test_case in range(1, T + 1):
    cases = input().split()
    stack = []
    try:
        for i in range(len(cases)-1):
                if cases[i].isdigit():
                    stack.append(int(cases[i]))
                    continue
                else:
                    a = stack.pop()
                    b = stack.pop()
                    if cases[i] == '+':
                        stack.append(b+a)
                        continue
                    elif cases[i] == '-':
                        stack.append(b-a)
                    elif cases[i] == '*':
                        stack.append(b*a)
                    else:
                        # //
                        if not b or not a:
                            stack.append(0)
                        else:
                            stack.append(b//a)
        res = stack.pop()
        if stack:
            print(f'#{test_case} error')
        else:
            print(f'#{test_case} {res}')
    except:
        print(f'#{test_case} error')







