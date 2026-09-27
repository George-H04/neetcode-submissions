class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        output = tokens[0]
        stack = []

        for c in tokens:
            try:
                value = int(c)
                stack.append(value)
            except ValueError:
                x = int(stack.pop())
                y = int(stack.pop())

                if c == '+':
                    output = (x + y)
                elif c == '*':
                    output = x * y
                elif c == '-':
                    output = y - x
                else:
                    output = y / x
                stack.append(output)

        return int(output)