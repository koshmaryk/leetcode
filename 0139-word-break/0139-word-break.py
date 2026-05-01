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
        memo = {}

        def dp(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for word in wordDict:
                if s[i:i + len(word)] == word and dp(i + len(word)):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dp(0)
