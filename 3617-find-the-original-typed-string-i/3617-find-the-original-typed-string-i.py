class Solution:
    # a b b c c c c
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        count = 0
        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                ans += 1
        return ans
