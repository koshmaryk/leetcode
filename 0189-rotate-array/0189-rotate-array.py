class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4,5,6,7]
        # [5,6,7,1,2,3,4]
        # k = 3
        def rotateHelper(l: int, r: int) -> None:
            while (l < r):
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        n = len(nums)
        k = k % n
        rotateHelper(0, n - 1)
        rotateHelper(0, k - 1)
        rotateHelper(k, n - 1)