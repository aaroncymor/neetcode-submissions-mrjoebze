class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        left = 0
        for right in range(1, len(prices)):
            print(right, left)
            if prices[right] < prices[left]:
                left = right
            else:
                maxP = max(maxP, prices[right] - prices[left])
        return maxP