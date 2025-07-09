class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append((price, ans))
        return ans

#  0 1 2 3 4 
# [7,2,1,2,2]
# stack = [(7,1),(2,4)]
# 
# [1,1,1,3,4]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)