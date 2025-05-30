import heapq

class Solution:
    # ans = [1]
    # heapq = [1]
    # |
    # 1 -1
    # 0  1
    #
    #
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
        window = []
        for i in range(0, k):
            window.append((-nums[i], i))
        heapq.heapify(window)
        ans.append(-window[0][0])

        for i in range(k, len(nums)):
            while window and window[0][1] <= i - k:
                heapq.heappop(window)
            heapq.heappush(window, (-nums[i], i))
            ans.append(-window[0][0])
        return ans