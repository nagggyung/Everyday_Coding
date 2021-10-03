class Solution:
    def toMatch(self, c: str) ->str:
        if c == ')':
            return '('
        if c == ']':
            return '['
        if c== '}':
            return '{'
    
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s:
            if len(stack)==0:
                stack.append(ch)
            elif ch == '(' or ch == '[' or ch == '{':
                 stack.append(ch)
            else:
                match_ch = self.toMatch(ch)
                last_ch = stack[-1]
                if match_ch == last_ch:
                    stack.pop()
                else:
                    return False
        
        if len(stack)==0:
            return True 
        
