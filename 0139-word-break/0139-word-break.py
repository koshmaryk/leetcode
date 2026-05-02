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
        
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            curr = root
            for j in range(i, n):
                c = s[j]
                curr = curr.children.get(c)
                if not curr:
                    break

                if curr.is_word and dp[j + 1]:
                    dp[i] = True
                    break

            # for word in wordDict:
            #     end = i + len(word)
            #     if end <= n and s[i:end] == word and dp[end]:
            #         dp[i] = True
            #         break
        return dp[0]
