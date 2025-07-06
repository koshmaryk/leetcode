class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        seq = [0] * 26
        for i, c in enumerate(order):
            seq[ord(c) - ord('a')] = i

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if seq[ord(words[i][j]) - ord('a')] > seq[ord(words[i + 1][j]) - ord('a')]:
                        return False
                    break
        return True
