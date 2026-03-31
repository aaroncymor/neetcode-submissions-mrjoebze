class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_ctr = 0
        for n in nums:
            if n == 0:
                zero_ctr += 1
                continue
            total *= n
        
        if zero_ctr > 1:
            return [0] * len(nums)
        
        res = []
        for n in nums:
            if zero_ctr:
                if n == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total // n)
        return res