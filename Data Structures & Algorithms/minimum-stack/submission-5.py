class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = float('inf')

    def push(self, val: int) -> None:
        self.current_min = min(val, self.current_min)
        self.stack.append((val, self.current_min))

    def pop(self) -> None:
        self.stack.pop(-1)

        if self.stack:
            self.current_min = self.stack[-1][1]
        else:
            self.current_min = float('inf')
            

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
