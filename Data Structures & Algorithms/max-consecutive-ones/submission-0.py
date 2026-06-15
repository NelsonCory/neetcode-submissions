class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currCount = 0
        for i in nums:
            if i == 1:
                currCount +=1
            else:
                if currCount > maxCount:
                    maxCount = currCount
                currCount = 0
        if currCount > maxCount:
            maxCount = currCount
        return maxCount
