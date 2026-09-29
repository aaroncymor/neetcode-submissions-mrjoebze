import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sub = []

        for num in nums:
            idx = bisect.bisect_left(sub, num)

            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        
        return len(sub)

