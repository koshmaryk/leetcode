from collections import deque

class Solution:
    # ans = [3,3,5,5,6,7]
    # deque = [7]
    # 
    # 
    #                  l     r
    # 1, 3, -1, -3, 5, 3, 6, 7
    # 0  1   2  3   4  5  6  7
    #
    # keep window boundary valid -> deque <- keep window ordered
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        window = deque([])
        l = 0
        for r in range(len(nums)):
            while window and nums[window[-1]] <= nums[r]:
                window.pop()

            window.append(r)

            if l > window[0]:
                window.popleft()

            if r + 1 >= k:
                output.append(nums[window[0]])
                l += 1
        
        return output