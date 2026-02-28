from collections import defaultdict

class Solution:
    '''
    3 2 1 0 0 ... 

    axbcd

    cxacd



    

    '''
    def customSortString(self, order: str, s: str) -> str:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1
        
        permutation = []
        for c in order:
            if c in counter:
                permutation.append(c * counter.pop(c))

        for c,freq in counter.items():
            permutation.append(c * freq)
        return ''.join(permutation)
