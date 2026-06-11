class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visitedDict = {}
        for i in nums:
            if visitedDict.get(i):
                return True
            else:
                visitedDict[i] = True
        return False