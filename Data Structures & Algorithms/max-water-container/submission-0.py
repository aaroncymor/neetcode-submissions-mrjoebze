class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                minHeight = min(heights[i], heights[j])
                maxA = max(maxA, minHeight * (j - i))
        return maxA
