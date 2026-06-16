class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = {}
        for i in range(len(nums)):
            if(nums[i] in targetDict):
                return [targetDict.get(nums[i]),i]
            else:
                targetDict[target-nums[i]] = i
        return []