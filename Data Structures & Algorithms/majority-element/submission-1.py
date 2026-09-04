class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countDict = {}

        for i in nums:
            if countDict.get(i,0):
                countDict[i] += 1
            else:
                countDict[i] = 1
                        
        maxValue = nums[0]
        for i in tuple(countDict.keys()):
            if countDict[i] > countDict[maxValue]:
                maxValue = i
        print(countDict)
        return maxValue