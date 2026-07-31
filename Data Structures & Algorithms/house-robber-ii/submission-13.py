class Solution:
    def rob1(self, nums: List[int]) -> int:

        prev2, prev1 = 0, 0
        for num in nums:

            curr = max(prev2 + num , prev1)
            prev2 = prev1
            prev1 = curr
        
        return prev1

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))