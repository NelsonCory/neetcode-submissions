class Solution:
    stack = []

    def clearStack(self):
        self.stack = []

    def plusOperation(self):
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        val3 = val1+val2
        self.stack.append(int(val2))
        self.stack.append(int(val1))
        self.stack.append(int(val3))
    
    def dOperation(self):
        self.stack.append(self.stack[-1]*2)

    def cOperation(self):
        self.stack.pop()

    def numOperation(self,val):
        self.stack.append(int(val))

    def calPoints(self, operations: List[str]) -> int:
        self.clearStack()
        for i in operations:
            print(i,self.stack)
            if i == '+':
                self.plusOperation()
            elif i == 'D':
                self.dOperation()
            elif i == 'C':
                self.cOperation()
            else:
                self.numOperation(i)
        print(self.stack)
        return sum(self.stack)