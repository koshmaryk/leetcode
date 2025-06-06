class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #    |
        # [1,2,3,0,0,0]
        #|
        # [2,5,6]
        #        |
        # [1,2,2,3,5,6]
        p1, p2 = m - 1, n - 1
        for p in range(m + n - 1, -1, -1):
            if p2 < 0:
                break

            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

        #    |
        # [2,0]
        #  |
        # [1]
        #    |
        # [2,0]