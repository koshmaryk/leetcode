"""
leet

leet + "" (empty base case)
lee + t
le + e; l + ee
l + e; e + e

le + et
l + eet

s[i:i + len(word)] == word and dp[i + len(word)]

leet, code


leetcode
i=0=l
   j=3=t -> is_word
    j+1=4=c = True
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        memo = {}
        def canBreak(i):
            if i < 0:
                return True

            if i in memo:
                return memo[i]

            for word in wordDict:
                if s[i - len(word) + 1:i + 1] == word and canBreak(i - len(word)):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return canBreak(len(s) - 1)
