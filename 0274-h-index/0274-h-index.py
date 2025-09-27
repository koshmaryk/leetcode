class Solution:
    ''' 
    3,0,6,1,5

    6,5,3,1,0

    '''
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) # 6,5,3,1,0
        h = 0
        for i, citation in enumerate(citations): # 0,6 | 1,5 | 2,3 | 3,1 | ... 
            if citation >= i + 1:
                h = i + 1 # 1 | 2 | 3 | 3 ...
        return h
