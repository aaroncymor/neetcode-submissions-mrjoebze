class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minNum = nums[left]

        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                if nums[left] < nums[right]:
                    minNum = min(minNum, nums[left])
                    break
            
            minNum = min(minNum, nums[mid])
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1

        return minNum