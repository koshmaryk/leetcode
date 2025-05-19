class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        i, j = 0, 0
        word = []
        while i < n or j < m:
            if i < n:
                word.append(word1[i])
                i += 1
            if j < m:
                word.append(word2[j])
                j += 1
        return "".join(word)

        