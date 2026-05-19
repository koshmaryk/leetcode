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
"""
from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        words = set(wordDict)

        seen = set()
        queue = deque([0])
        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if s[start:end] in words and end not in seen:
                    queue.append(end)
                    seen.add(end)
        return False
        