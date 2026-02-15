class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = []
        for idx, num in enumerate(nums):
            if num != 0:
                self.nonzero.append((idx, num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        p, q = 0, 0
        while p < len(self.nonzero) and q < len(vec.nonzero):
            if self.nonzero[p][0] < vec.nonzero[q][0]:
                p += 1
            elif self.nonzero[p][0] > vec.nonzero[q][0]:
                q += 1
            else:
                product += self.nonzero[p][1] * vec.nonzero[q][1]
                p += 1
                q += 1
        return product
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)