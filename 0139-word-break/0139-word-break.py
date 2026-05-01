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
        words = set(wordDict)

        memo = {}

        def can_break(word):
            if not word:
                return True

            if word in memo:
                return memo[word]

            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in words and can_break(word[i:]):
                    memo[word] = True
                    return True

            memo[word] = False
            return False
            
        return can_break(s)
