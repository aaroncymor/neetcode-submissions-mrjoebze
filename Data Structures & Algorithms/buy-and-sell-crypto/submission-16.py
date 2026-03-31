class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left = 0

        for right in range(len(prices)):
            if prices[right] <= prices[left]:
                left = right
            maxP = max(maxP, prices[right] - prices[left])
            right += 1
        return maxP