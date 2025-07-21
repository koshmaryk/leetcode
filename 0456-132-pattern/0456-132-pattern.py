class Solution:
    '''
        nums 1,3,1,2,2
    min_nums 1 1 1 1 1


        nums 3,1,4,2,0

    min_nums 3 1 1 1 0

stack = [2]       
    '''
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
    
        min_nums = [0] * n
        min_nums[0] = nums[0]
        for i in range(1, n):
            min_nums[i] = min(min_nums[i - 1], nums[i])

        stack = []
        for j in range(n - 1, -1, -1):
            if nums[j] <= min_nums[j]:
                continue

            while stack and stack[-1] <= min_nums[j]: # nums[j] > minimum for nums[j]
                stack.pop()

            while stack and stack[-1] < nums[j]: # nums[k] < nums[j]
                return True

            stack.append(nums[j])
        
        return False