class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        left = 0
        right = len(nums) - 1
        minNum = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                if nums[left] < nums[right]:
                    minNum = min(minNum, nums[left])
                    break

            minNum = min(minNum, nums[mid])
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return minNum
