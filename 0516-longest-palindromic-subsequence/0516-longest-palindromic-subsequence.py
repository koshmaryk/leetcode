"""

s[l]==s[r] -> dfs(l+1,r-1) + 2 # l,r

max(dfs(l+1:r), dfs(l:r-1))

if l > r: return 0
if l == r: return 1

dfs(0, n - 1) # l,r

01234
bbbab

i=4 skip
i=3,j=4
i=2,j=3
i=2,j=4
i=1,j=2
i=1,j=3
i=1,j=4
i=0,j=1
i=0,j=2
i=0,j=3
i=0,j=4

  0 1 2 3 4
0 1 2 3 3 4
1 0 1 2 2 3
2 0 0 1 1 3
3 0 0 0 1 1
4 0 0 0 0 1

"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]