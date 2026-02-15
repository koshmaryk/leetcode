class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = []
        for idx, num in enumerate(nums):
            if num != 0:
                self.nonzero.append((idx, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        sparse, dense = self.nonzero, vec.nonzero
        if len(sparse) > len(dense):
            sparse, dense = dense, sparse

        for p, num1 in sparse:
            num2 = self.bisect(dense, p)
            if num2 != -1:
                product += num1 * num2
        return product

    def bisect(self, arr: List[Tuple[int, int]], target: int):
        bad, good = -1, len(arr)
        while good - bad > 1:
            mid = (bad + good) // 2
            if arr[mid][0] >= target:
                good = mid
            else:
                bad = mid
        return -1 if good == len(arr) or arr[good][0] != target else arr[good][1]
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)