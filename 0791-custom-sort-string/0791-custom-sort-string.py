class Solution:
    '''
    3 2 1 0 0 ... 

    axbcd

    cxacd



    

    '''
    def customSortString(self, order: str, s: str) -> str:
        priority = {}
        for i, c in enumerate(order):
            priority[c] = i
        return ''.join(sorted(s, key=lambda x: priority.get(x, 26)))
     