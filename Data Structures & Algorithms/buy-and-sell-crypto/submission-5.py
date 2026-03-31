class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)

        return maxP


