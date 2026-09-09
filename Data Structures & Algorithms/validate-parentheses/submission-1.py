class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{":"}","[":"]","(":")"}
        stack = []

        for i in s:
            if pairs.get(i,0):
                #if an opening bracket
                stack.append(i)
            else:
                #if a closing bracket
                if len(stack) and pairs.get(stack[-1],0) == i:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0