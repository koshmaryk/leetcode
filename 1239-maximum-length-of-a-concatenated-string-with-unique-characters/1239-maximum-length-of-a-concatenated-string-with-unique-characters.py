'''
['un', 'iq', 'ue'] # un, unw

'', 'un', 'iq', 'uniq', 'ue', 'ique'


'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        results = ['']
        best = 0

        for word in arr:
            for i in range(len(results)):
                cand = results[i] + word
                if len(cand) != len(set(cand)):
                    continue

                results.append(cand)
                best = max(best, len(cand))
        return best