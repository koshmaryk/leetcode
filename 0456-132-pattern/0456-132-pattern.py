class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        min_i = [0] * n
        min_i[0] = nums[0]
        for j in range(1, n):
            min_i[j] = min(min_i[j - 1], nums[j])

        stack = []
        for j in range(n - 1, -1, -1):
            if nums[j] > min_i[j]:
                while stack and stack[-1] <= min_i[j]: # nums[k] > nums[i]
                    stack.pop()

                if stack and stack[-1] < nums[j]:      # nums[k] < nums[j]
                    return True

                stack.append(nums[j])
        return False