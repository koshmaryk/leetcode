from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        count = Counter(arr)
        for k,v in count.items():
            if v > n // 4:
                return k
        return -1
