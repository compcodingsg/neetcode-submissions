class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        n = len(prices)
        profit = 0
        while r < n:
            profit = max(profit, prices[r]-prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1
        return profit