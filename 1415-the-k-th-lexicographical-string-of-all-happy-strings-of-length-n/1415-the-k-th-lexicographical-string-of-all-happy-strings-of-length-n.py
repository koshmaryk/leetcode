"""
    a           b           c
 b     c      a    c      a    b
a c   a b    b c   a b   b c  a c  

n = 3
k = 6 # 0-indexed

each letter owns block of size 2^(n-1) = 2^2 = 4

6 // 4 = 1
k = 6 % 4 = 2

"""
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * (1 << (n - 1))
        if k > total:
            return ""

        k -= 1

        s = []
        block = 1 << (n - 1)
        s.append("abc"[k // block])
        k %= block

        for _ in range(n - 1):
            block >>= 1 # 2^(n-2), 2^(n-3), ...
            choices = [c for c in "abc" if c != s[-1]]
            s.append(choices[k // block])
            k %= block
        
        return "".join(s)
