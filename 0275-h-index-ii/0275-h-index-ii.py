class Solution:
    '''
    0 1 2 3 4

    0,1,3,5,6

    n=5; 


    '''
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        ans = 0
        for i, citation in enumerate(citations):
            if citation >= n - i:
                ans = n - i
                break
        return ans