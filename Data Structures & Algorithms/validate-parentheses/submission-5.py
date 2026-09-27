class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['(', '{', '[']
        closed = [')', '}', ']']

        stack = []

        for c in s:
            if not stack and c in closed:
                return False
            if c in opened:
                stack.append(c)
            if c in closed and stack:
                if c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            

        return not stack