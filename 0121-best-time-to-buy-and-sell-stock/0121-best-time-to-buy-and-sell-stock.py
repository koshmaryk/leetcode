class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10**5
        max_profit = 0
        # min_price = 1
        # max_profit = 0
        #         |
        # 7,6,4,3,1
        #         |
        # 7,1,5,3,6,4
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit

