class Solution:
    #    1  2  3 4
    # 1  1  2  6 24
    # 24 24 12 4 1
    # 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        p = [1] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] * nums[i]

        s = [1] * (n + 1)
        for i in range(n - 1, -1, -1):
            s[i] = s[i + 1] * nums[i]

        for i in range(n):
            answer[i] = p[i] * s[i + 1]
        
        # (product to the left of i) * (product to the right of i)
        return answer