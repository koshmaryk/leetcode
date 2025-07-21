class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        bad, good = -1, len(arr) - 1
        while good - bad > 1:
            mid = (bad + good) // 2
            if arr[mid] > arr[mid + 1]:
                good = mid
            else:
                bad = mid
        return good