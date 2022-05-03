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

def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        
        # 여는 괄호 만나면 스택에 push()
        if c in '({[':
            S.push(c)
        
        # 닫는 괄호 만난 경우
        elif c in match:
            # 스택이 비어 있으면 올바르지 않은 수식
            if S.isEmpty():
                return False
            # 스택에서 pop, 쌍을 이루는 괄호인지 검사
            else:
                t = S.pop()

                if t != match[c]:
                    return False
    # 끝까지 검사한 후, 스택이 비어있어야 올바른 수식. 
    return S.isEmpty()