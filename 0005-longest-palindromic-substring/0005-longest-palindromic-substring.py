class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return [l + 1, r - 1]


        ans = [0, 0]
        for i in range(n):
            odd = expand(i, i)
            if odd[1] - odd[0] > ans[1] - ans[0]:
                ans = odd

            even = expand(i, i + 1)
            if even[1] - even[0] > ans[1] - ans[0]:
                ans = even
        
        l, r = ans
        return s[l:r + 1]
