class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k >= len(arr): return arr
        if x <= arr[0]: return arr[:k]
        if x >= arr[-1]: return arr[-k:]
        bad, good = -1, len(arr) - k
        while good - bad > 1:
            mid = (bad + good) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                good = mid
            else:
                bad = mid
        return arr[good:good + k]