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

"""
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

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

        memo = {}

        def can_break(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            curr = root
            for j in range(i, n):
                c = s[j]
                curr = curr.children.get(c)
                if not curr:
                    break

                if curr.is_word and can_break(j + 1):
                    memo[j] = True
                    return True     

            # for word in wordDict:
            #     if s[i:i + len(word)] == word and can_break(i + len(word)):
            #         memo[i] = True
            #         return True

            memo[i] = False
            return False

        return can_break(0)
