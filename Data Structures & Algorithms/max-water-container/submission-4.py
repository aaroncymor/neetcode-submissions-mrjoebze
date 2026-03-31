class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                maxA = max(maxA, (j-i) * min(heights[i], heights[j]))
        return maxA