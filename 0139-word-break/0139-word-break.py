"""
N is length of s, M is length of wordDict, and L is max length of word in wordDict
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

01234567
leetcode
dp[8] = True
dp[4] = True
dp[0] = True

"""
from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                end = i + len(word)
                if end <= n and s[i:i + len(word)] == word and dp[end]:
                    dp[i] = True
                    break
        return dp[0]
        