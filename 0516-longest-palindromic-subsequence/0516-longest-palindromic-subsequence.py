"""

s[l]==s[r] -> dfs(l+1,r-1) + 2 # l,r

max(dfs(l+1:r), dfs(l:r-1))

if l > r: return 0
if l == r: return 1

dfs(0, n - 1) # l,r

"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        memo = {}

        def dfs(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if l > r:
                return 0
            if l == r:
                return 1

            if s[l] == s[r]:
                memo[(l, r)] = dfs(l+1, r-1) + 2
            else:
                memo[(l, r)] = max(dfs(l, r-1), dfs(l+1, r))

            return memo[(l, r)]

        return dfs(0, n-1)
        