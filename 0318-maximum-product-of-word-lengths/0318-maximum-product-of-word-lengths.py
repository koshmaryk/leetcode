class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def no_common_letters(word1, word2):
            for c in word1:
                if c in word2:
                    return False
            return True

        n = len(words)
        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if no_common_letters(words[i], words[j]):
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product
        