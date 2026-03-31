class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        counted = {}
        for n in nums:
            counted[n] = counted.get(n, 0) + 1
        res = []

        for i in range(len(nums)):
            counted[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                counted[nums[j]] -= 1

                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if target in counted and counted[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                counted[nums[j]] += 1

        return res




