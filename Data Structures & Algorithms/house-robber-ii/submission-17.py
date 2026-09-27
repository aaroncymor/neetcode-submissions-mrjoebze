class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob1(nums: List[int]) -> int:
    
            one, two = 0, 0
            for i in range(len(nums)):
                temp = max(nums[i] + one, two)
                one = two
                two = temp
            return two 

        if len(nums) == 1:
            return nums[0]

        res1 = rob1(nums[1:])
        res2 = rob1(nums[:-1])
        return max(res1, res2)