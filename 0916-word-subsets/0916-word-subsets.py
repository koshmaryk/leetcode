class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        def count(word):
            counter = [0] * 26
            for c in word:
                counter[ord(c) - ord('a')] += 1
            return counter

        bmax = [0] * 26
        for b in words2:
            for i, cnt in enumerate(count(b)):
                bmax[i] = max(bmax[i], cnt)
        
        output = []
        for a in words1:
            if all(x >= y for x, y in zip(count(a), bmax)):
                output.append(a)
        return output