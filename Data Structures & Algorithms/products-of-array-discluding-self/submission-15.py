class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCtr = 0

        for num in nums:
            if not num:
                zeroCtr += 1
            else:
                prod *= num
        
        if zeroCtr > 1:
            return [0] * len(nums)
        
        res = []
        for num in nums:
            if not num and zeroCtr:
                res.append(prod)
            else:
                if zeroCtr:
                    res.append(0)
                else:
                    res.append(prod // num)
        return res