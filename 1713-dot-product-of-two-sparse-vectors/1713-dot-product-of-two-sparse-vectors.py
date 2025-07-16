class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = []
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzero.append((i, n))
        

    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.nonzero) < len(vec.nonzero):
            smaller, larger = self, vec
        else:
            smaller, larger = vec, self

        result = 0
        for i, n in smaller.nonzero:
            j = self.binary_search(larger.nonzero, i)
            if j != -1:
                result += n * larger.nonzero[j][1]
        
        return result

    def binary_search(self, arr: List[Tuple[int, int]], target: int) -> int:
        bad, good = -1, len(arr)
        while good - bad > 1:
            mid = (bad + good) // 2
            if arr[mid][0] >= target:
                good = mid
            else:
                bad = mid
        return -1 if good == len(arr) or arr[good][0] != target else good


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)