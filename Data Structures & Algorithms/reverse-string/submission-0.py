class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        leftIndex = 0
        rightIndex = len(s)-1

        while leftIndex < rightIndex:
            temp = s[rightIndex]
            s[rightIndex] = s[leftIndex]
            s[leftIndex] = temp
            leftIndex += 1
            rightIndex -= 1
            