from collections import deque

class Solution:
    # ans = []
    # deque = [(11, 1),]
    #   |
    # 9 11
    # 0  1
    #
    #
    # ans = [3,3,5,5,6,7]
    # deque = [(7, 7),]
    #                        |
    # 1, 3, -1, -3, 5, 3, 6, 7
    # 0  1   2  3   4  5  6  7
    #
    # keep window boundary valid -> deque <- keep window ordered
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        window_max = deque([])
        l = 0
        for r in range(len(nums)):
            while window_max and nums[window_max[-1]] < nums[r]:
                window_max.pop()

            window_max.append(r)

            if l > window_max[0]:
                window_max.popleft()

            if r + 1 >= k:
                output.append(nums[window_max[0]])
                l += 1
        
        return output