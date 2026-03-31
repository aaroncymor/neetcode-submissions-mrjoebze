class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeroCtr = 0
        for num in nums:
            if not num:
                zeroCtr += 1
            else:
                total *= num
        
        if zeroCtr > 1:
            return [0] * len(nums)
        
        res = []
        for num in nums:
            if zeroCtr:
                if not num:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(total // num)
        return res