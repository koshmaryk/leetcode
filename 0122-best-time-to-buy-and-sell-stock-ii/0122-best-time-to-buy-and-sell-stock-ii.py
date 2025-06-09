class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #
        # 7,1,5,6,3,6,4
        #           l r
        # 
        max_profit = 0 # 4 + 1 + 3
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                max_profit += prices[r] - prices[l]
                l = r
            r += 1
        return max_profit