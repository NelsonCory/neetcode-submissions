class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        newString = ""
        leftLen = len(word1)
        rightLen = len(word2)
        while left < leftLen and right < rightLen:
            newString += word1[left] + word2[right]
            left += 1
            right += 1
        if rightLen != leftLen:
            if max(leftLen,rightLen) == leftLen:
                newString += word1[rightLen:]
            else:
                newString += word2[leftLen:]
        return newString