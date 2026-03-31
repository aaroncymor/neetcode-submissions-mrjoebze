class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            if heights[left] <= heights[right]:
                maxA = max(maxA, (right - left) * heights[left])
                left += 1
            else:
                maxA = max(maxA, (right - left) * heights[right])
                right -= 1
        return maxA
