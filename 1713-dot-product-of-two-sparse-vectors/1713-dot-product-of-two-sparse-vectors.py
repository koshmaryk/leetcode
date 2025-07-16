class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzero[i] = n
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, n in self.nonzero.items():
            if i in vec.nonzero:
                result += n * vec.nonzero[i]
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)