"""
leet

leet + "" (empty base case)
lee + t
le + e; l + ee
l + e; e + e

le + et
l + eet

s[i:i + len(word)] == word and dp[i + len(word)]


"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        memo = {}

        def can_break(i):
            if i < 0:
                return True

            if i in memo:
                return memo[i]

            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and can_break(i - len(word)):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return can_break(len(s) - 1)
