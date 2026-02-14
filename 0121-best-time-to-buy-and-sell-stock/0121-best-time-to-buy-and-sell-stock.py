class Solution:
    '''
    7,1,5,3,6,4
    
    ans = 0



    '''
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                ans = max(ans, prices[r] - prices[l])
            r += 1
        return ans