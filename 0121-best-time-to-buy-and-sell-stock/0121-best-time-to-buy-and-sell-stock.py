class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l, r = 0, 1 # buy pointer, sell pointer
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
            r += 1

        return max_profit
