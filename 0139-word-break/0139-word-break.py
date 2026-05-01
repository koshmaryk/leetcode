"""
leet

leet + "" (empty base case)
lee + t
le + e; l + ee
l + e; e + e

le + et
l + eet



"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                end = i + len(word)
                if end <= n and s[i:end] == word and dp[end]:
                    dp[i] = True
                    break
        return dp[0]
