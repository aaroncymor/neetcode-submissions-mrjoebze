class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        nums.sort()
        count = {}
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if target in count and count[target] > 0:
                    res.append([nums[i], nums[j], target])
            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res




