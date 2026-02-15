class Solution:
    # babad
    # b, ba, bab, baba, babad
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        i, j = 0, 0
        for k in range(n):
            odd = expand(k, k)
            if odd[1] - odd[0] > j - i:
                i, j = odd

            even = expand(k, k + 1)
            if even[1] - even[0] > j - i:
                i, j = even

        return s[i : j + 1]
        
        