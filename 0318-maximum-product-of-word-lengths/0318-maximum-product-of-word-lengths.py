class Solution:
    def maxProduct(self, words: List[str]) -> int:
        char_sets = [set(word) for word in words]

        n = len(words)
        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if not (char_sets[i] & char_sets[j]):
                    max_product = max(max_product, len(words[i]) * len(words[j]))
        return max_product
        