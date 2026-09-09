class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        for i in tokens:
            if i not in ["+","-","/","*"]:
                self.stack.append(int(i))
            else:
                self.performOperation(i)
        return self.stack[-1]
        

    def performOperation(self,operation):
        val2 = self.stack.pop()
        val1 = self.stack.pop()
        if operation == "+":
            self.stack.append(val1+val2)
        elif operation == "-":
            self.stack.append(val1-val2)
        elif operation == "*":
            self.stack.append(val1*val2)
        else:
            self.stack.append(int(val1 / val2))