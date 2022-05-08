'''
중위 수식 -> 후위 수식

0. 피연산자인 경우 그냥 push

1. '(' 이면 스택에 push

2. 연산자의 우선순위 설정
우선순위가 높거나 같으면 pop, 아닌 경우 push(현재 연산자)
 -- >2-1. 스택이 비어있지 않는 동안
-- > 2-2 스택이 비어 있으면 연산자 push

3. ')' 이면 '(' 나올 때 까지 pop()

4. 수식 끝까지 간 후 에 스택에 남아있는 연산자는 모두 pop 출력
'''

class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''

    for s in S:
        # 0. 피 연산자인 경우 그냥 push
        if s.isalpha():
            answer += s
            continue

        #1. '(' 이면 스택에 push
        if s == '(':
            opStack.push(s)
            continue

        #2. 우선순위가 높거나 같으면 pop, 아닌 경우 push
        if s in prec:

            # opStack이 비어있지 않는 동안
            while not opStack.isEmpty():
                print(True)
                if prec[opStack.peek()] >= prec[s]:
                    answer += opStack.pop()
                    continue

                else:
                    opStack.push(s)
                    break
            # opStack이 비어 있으면 연산자 push
            if opStack.isEmpty():
                opStack.push(s)


        # 3. ')' 이면 '(' 나올 때 까지 pop()
        if s == ')':
            while not opStack.isEmpty():
                if opStack.peek() != '(':
                    answer += opStack.pop()
                else:
                    opStack.pop()
                    break

    # 4. 수식 끝까지 간 후에 스택에 남아있는 연산자는 모두 pop 출력
    while not opStack.isEmpty():
        answer += opStack.pop()


    return answer

res = solution("(A+B)*C")
print(res)