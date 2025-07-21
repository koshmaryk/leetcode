class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        encoded = []

        p1, p2 = 0, 0 # encoded1, encoded2
        freq1, freq2 = encoded1[0][1], encoded2[0][1]
        while p1 < len(encoded1) and p2 < len(encoded2):
            val1, val2 = encoded1[p1][0], encoded2[p2][0]

            val = val1 * val2
            min_freq = min(freq1, freq2)

            freq1 -= min_freq
            if freq1 == 0:
                p1 += 1
                freq1 = encoded1[p1][1] if p1 < len(encoded1) else 0

            freq2 -= min_freq
            if freq2 == 0:
                p2 += 1
                freq2 = encoded2[p2][1] if p2 < len(encoded2) else 0

            if not encoded or encoded[-1][0] != val:
                encoded.append([val, min_freq])
            else:
                encoded[-1][1] += min_freq
        return encoded
