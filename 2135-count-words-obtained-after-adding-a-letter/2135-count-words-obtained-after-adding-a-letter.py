"""

100101


"""
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        words = set(["".join(sorted(start)) for start in startWords])

        ans = 0
        for target in targetWords:
            t = "".join(sorted(target))
            for i in range(len(t)):
                if t[:i] + t[i + 1:] in words:
                    ans += 1
                    break
        return ans
        