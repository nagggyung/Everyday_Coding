'''
1. for 문 돌면서 피 연산자인 경우 스택에 push 
2. 연산자 만나면 스택에서 pop --> 1 pop --> 2
(2) 연산자 (1) 을 계산 후 이 결과를 스택에 push 

3. 수식의 끝에 도달하면 스택에서 pop

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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


# 중위 표현식 -- >  후위 표현 식
def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []

    for token in tokenList:
        if type(token) is int:
            postfixList.append(token)

        if token == '(':
            opStack.push(token)
            continue
        if token in prec:
            while not opStack.isEmpty():
                if prec[opStack.peek()] >= prec[token]:
                    postfixList.append(opStack.pop())
                    continue
                else:
                    opStack.push(token)
                    break

            if opStack.isEmpty():
                opStack.push(token)

        if token == ')':
            while not opStack.isEmpty():
                if opStack.peek() != '(':
                    postfixList.append(opStack.pop())
                else:
                    opStack.pop()
                    break

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    opList = ['*', '/', '+', '-']
    opStack = ArrayStack()
    res = 0

    for token in tokenList:
        if type(token) is int:
            opStack.push(token)
            continue
            
        if str(token) in opList:
            val1 = opStack.pop()
            val2 = opStack.pop()
            if token == '*':
                opStack.push(val2 * val1)
            elif token == '/':
                opStack.push(val2 / val1)
            elif token == '+':
                opStack.push(val2 + val1)
            else:
                opStack.push(val2 - val1)

    if not opStack.isEmpty():
        res = opStack.pop()
    return res


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)

    return val