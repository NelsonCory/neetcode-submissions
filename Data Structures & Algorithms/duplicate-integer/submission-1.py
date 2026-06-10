class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in nums:
            if hashmap.get(i) != None:
                return True
            else:
                hashmap[i] = True
        return False