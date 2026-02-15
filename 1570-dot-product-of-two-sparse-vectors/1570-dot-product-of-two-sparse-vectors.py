class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.nonzero[i] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        a, b = self.nonzero, vec.nonzero
        if len(a) > len(b):
            a, b = b, a

        for k in a.keys():
            if k in b:
                product += b[k] * a[k]
        return product
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)