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
from collections import deque

class TrieNode:
    def __init__(self,):
        self.children = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        root = TrieNode()
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True

        seen = set()
        queue = deque([0])
        while queue:
            i = queue.popleft()
            if i == n:
                return True

            curr = root
            for j in range(i, n):
                c = s[j]
                curr = curr.children.get(c)
                if not curr:
                    break

                if curr.is_word and (j + 1) not in seen:
                    seen.add(j + 1)
                    queue.append(j + 1)
        return False


        