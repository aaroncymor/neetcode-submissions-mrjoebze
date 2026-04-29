class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_ctr = 0
        for n in nums:
            if not n:
                zero_ctr += 1
                continue

            if zero_ctr > 1:
                return [0] * len(nums)
            
            total *= n

        res = []
        for n in nums:
            if zero_ctr:
                res.append(total) if not n else res.append(0)
            else:
                res.append(total // n)
        return res
            