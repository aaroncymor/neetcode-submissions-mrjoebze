class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        res = [] 
        res.append(nums[0])
        res.append(nums[1])

        for i in range(len(nums) - 3):
            res.append(res[i] + nums[i + 3])

        if len(res) == 2:
            return max(res)
        
        return res[-1]
