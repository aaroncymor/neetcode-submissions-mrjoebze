class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            if heights[left] <= heights[right]:
                maxArea = max(maxArea, (right - left) * heights[left])
                left += 1
            else:
                maxArea = max(maxArea, (right - left) * heights[right])
                right -= 1
        return maxArea