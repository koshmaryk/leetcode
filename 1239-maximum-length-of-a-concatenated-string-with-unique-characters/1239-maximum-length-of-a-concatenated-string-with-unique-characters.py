'''
['un', 'iq', 'ue'] # un, unw

'', 'un', 'iq', 'uniq', 'ue', 'ique'


'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        words = []
        for i in range(len(arr)):
            dup = False
            word = 0
            for c in arr[i]:
                mask = 1 << ord(c) - ord('a')
                if mask & word:
                    dup = True
                    break

                word |= mask

            if not dup:
                word |= len(arr[i]) << 26
                words.append(word)

        mask = (1 << 26) - 1
        results = [0]
        best = 0
        for word in words:
            old_bitset = word & mask
            old_length = word >> 26

            for i in range(len(results)):
                bitset = results[i] & mask
                length = results[i] >> 26

                if old_bitset & bitset:
                    continue

                word = old_bitset | bitset
                word |= (old_length + length) << 26
                results.append(word)
                best = max(best, old_length + length)

        return best
