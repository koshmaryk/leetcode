class Solution:
    def isHappy(self, n: int) -> bool:
        
        def next(n):
            next_n = 0
            while n > 0:
                digit = n % 10
                next_n += digit * digit
                n = n // 10
            return next_n

        slow = next(n)
        fast = next(next(n))
        while fast != 1:
            slow = next(slow)
            fast = next(next(fast))
            if slow == fast:
                return False
        return True
