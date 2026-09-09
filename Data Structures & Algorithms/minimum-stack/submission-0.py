class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not len(self.prefixStack):
            self.prefixStack.append(val)
        else:
            self.prefixStack.append(min(val, self.prefixStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.prefixStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefixStack[-1]
        
