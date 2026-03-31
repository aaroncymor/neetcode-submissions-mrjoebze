class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minBuy = prices[0]
        maxP = 0
        for price in prices:
            maxP = max(maxP, price - minBuy)
            minBuy = min(minBuy, price)
        return maxP
