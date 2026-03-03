from collections import defaultdict

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        masks = defaultdict(int)
        for word in words:
            mask = 0
            for c in word:
                mask |= 1 << (ord(c) - ord('a'))
            masks[mask] = max(masks[mask], len(word))

        max_product = 0
        for x in masks:
            for y in masks:
                if x & y == 0:
                    max_product = max(max_product, masks[x] * masks[y])
        return max_product
        