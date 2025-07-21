class Solution:
    '''
        0 1 2 3 4 5 6
        1,2,3,4,5,6,7

        0 1 2 3 4
        2,3,4,7,11 k = 2

        arr[i] - (i + 1)
        11 - (4 + 1) = 6 => 1,5,6,8,9

    '''
    def findKthPositive(self, arr: List[int], k: int) -> int:
        bad, good = -1, len(arr) # -1,5; 1,5; 3,5; 3,4
        l = []
        while good - bad > 1: # 6; 4; 3; 1
            mid = (bad + good) // 2 # 2; 3; 4; ...
            if arr[mid] - (mid + 1) >= k:
                good = mid
            else:
                bad = mid
        return good + k