class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nonzero[i] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for k in vec.nonzero.keys():
            if k in self.nonzero:
                product += self.nonzero[k] * vec.nonzero[k]
        return product
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)