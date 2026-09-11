class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        while lower <= upper:
            midpoint = (lower + upper) // 2
            #print(lower,upper, midpoint)
            if nums[midpoint] > target:
                upper = midpoint - 1
            elif nums[midpoint] < target:
                lower = midpoint + 1
            else:
                return midpoint
        return -1