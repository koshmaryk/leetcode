class Solution:
    #    1  2  3 4
    # 1  1  2  6 24
    # 24 24 12 4 1
    # 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        p = s = 1
        for i in range(n):
            answer[i] = p
            p *= nums[i]

        for i in range(n - 1, - 1, -1):
            answer[i] *= s 
            s *= nums[i]
        
        # (product to the left of i) * (product to the right of i)
        return answer