class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                maxP = max(maxP, prices[j] - prices[i])
        return maxP