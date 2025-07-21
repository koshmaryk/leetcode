class Solution:
    '''
        0 1 2 3 4 5 6
        1,2,3,4,5,6,7

        0 1 2 3 4
        2,3,4,7,11 k = 7

        arr[i] - (i + 1)
        11 - (4 + 1) = 6 => 1,5,6,8,9
    '''
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i in range(len(arr)):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k