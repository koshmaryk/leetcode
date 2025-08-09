class Solution:
    # babad
    # b, ba, bab, baba, babad
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def valid(i, j):
            l, r = i, j - 1
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        for length in range(n, 0, -1):
            for start in range(n - length + 1):
                if valid(start, start + length):
                    return s[start: start + length]

        return ""
        