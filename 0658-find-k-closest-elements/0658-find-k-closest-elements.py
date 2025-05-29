class Solution:
    # given a sorted input array, it means we have to answer "what's the optimal window position?"
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr): return arr
        if x <= arr[0]: return arr[:k]
        if x >= arr[-1]: return arr[-k:]

        bad, good = -1, len(arr) - k
        while good - bad > 1:
            mid = (bad + good) // 2
            # x ...arr[mid] ... | ... arr[mid + k]... x
            if x <= (arr[mid] + arr[mid + k]) // 2:
                good = mid
            else:
                bad = mid
        return arr[good:good + k]

# k = 4, x = 3
#                 
# -1 ... 1,2,3,4,5, ... 6,7,8,9 ... 10
#
# bad = -1, good = 0, mid = 2
# 3<=5?; 3<=3? 