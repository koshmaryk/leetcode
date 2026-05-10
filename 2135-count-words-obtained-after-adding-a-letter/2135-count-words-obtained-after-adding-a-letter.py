"""

TC O((N + M) * L)
SC O(M * L)


"""
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def mask(word):
            mask = 0
            for c in word:
                mask |= (1 << (ord(c) - ord('a')))
            return mask

        words = set()
        for start in startWords:
            s = mask(start)
            words.add(s)

        ans = 0
        for target in targetWords:
            t = mask(target)
            for c in target:
                if (t ^ (1 << (ord(c) - ord('a')))) in words:
                    ans += 1
                    break
        return ans
        