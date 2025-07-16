class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzero = []
        for i, n in enumerate(nums):
            if n != 0:
                self.nonzero.append((i, n))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        p, q = 0, 0
        while p < len(self.nonzero) and q < len(vec.nonzero):
            if self.nonzero[p][0] < vec.nonzero[q][0]:
                p += 1
            elif self.nonzero[p][0] > vec.nonzero[q][0]:
                q += 1
            else:
                result += self.nonzero[p][1] * vec.nonzero[q][1]
                p += 1
                q += 1
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)