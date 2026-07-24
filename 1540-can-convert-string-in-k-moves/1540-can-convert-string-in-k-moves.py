"""
s = "input", t = "ouput", k = 9

[0,1,2,3,4,5,6+26,7+26,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]



"""
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        n, m = len(s), len(t)
        if n != m:
            return False

        dist = list(range(26))
        for a,b in zip(s, t):
            if a == b:
                continue
            d = (ord(b) - ord(a)) % 26
            if dist[d] > k:
                return False
            dist[d] += 26
        return True
            