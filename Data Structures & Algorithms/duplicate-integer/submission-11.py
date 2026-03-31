class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        
        numSet = set()
        for n in nums:
            if n in numSet:
                return True
            numSet.add(n)
        return False