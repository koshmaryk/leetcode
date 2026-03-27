'''
['un', 'iq', 'ue'] # un, unw

'', 'un', 'iq', 'uniq', 'ue', 'ique'


'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        words = []
        for word in arr:
            dup = False
            bitset = 0
            for c in word:
                mask = 1 << ord(c) - ord('a')
                if mask & bitset:
                    dup = True
                    break

                bitset |= mask

            if not dup:
                words.append((bitset, len(word)))

        results = [(0, 0)]
        best = 0
        for curr_bitset, curr_length in words:
            for i in range(len(results)):
                bitset, length = results[i]

                if curr_bitset & bitset:
                    continue

                results.append((curr_bitset | bitset, curr_length + length))
                best = max(best, curr_length + length)

        return best
