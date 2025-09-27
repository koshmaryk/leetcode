class Solution:
    ''' 
    3,0,6,1,5

    1,1,0,1,0,2

    '''
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = [0] * (n + 1)
        for citation in citations:
            count[min(citation, n)] += 1

        p = 0
        for h in range(n, -1, -1):
            p += count[h]
            if p >= h:
                return h
        return 0
