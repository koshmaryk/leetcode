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
        ans = []
        window = deque()
        for i in range(0, len(nums)):
            while window and window[-1][0] < nums[i]:
                window.pop() # pop back, keep window ordered

            window.append((nums[i], i)) # push back

            while window and window[0][1] <= i - k:
                window.popleft() # pop front

            if i + 1 >= k: # first window onwards
                ans.append(window[0][0]) # answer for this window
        
        return ans