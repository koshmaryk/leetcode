class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = []
        self.indices = []
        for i, val in enumerate(nums):
            if val != 0:
                self.indices.append(i)
                self.nonzero.append(val)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if len(self.indices) < len(vec.indices):
            smaller, larger = self, vec
        else:
            smaller, larger = vec, self

        result = 0
        for i, idx in enumerate(smaller.indices):
            pos = self.binary_search(larger.indices, idx)
            if pos != -1:
                result += smaller.nonzero[i] * larger.nonzero[pos]
        
        return result

    def binary_search(self, arr: List[int], target: int) -> int:
        bad, good = -1, len(arr)
        while good - bad > 1:
            mid = (bad + good) // 2
            if arr[mid] >= target:
                good = mid
            else:
                bad = mid
        return -1 if good == len(arr) or arr[good] != target else good


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)