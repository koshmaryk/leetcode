'''
0,0,5,5,5,0,1,3,3

'''
class SparseVector:
    def __init__(self, nums: List[int]):
        self.ranges = []
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                start = i
                val = nums[i]
                while i < len(nums) and nums[i] == val:
                    i += 1
                self.ranges.append((start, i - 1, val))
            else:
                i += 1
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        p, q = 0, 0
        while p < len(self.ranges) and q < len(vec.ranges):
            s1, e1, v1 = self.ranges[p]
            s2, e2, v2 = vec.ranges[q]

            start = max(s1, s2)
            end = min(e1, e2)
            if start <= end:
                product += v1 * v2 * (end - start + 1)
            
            if e1 < e2:
                p += 1
            else:
                q += 1
        return product
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)