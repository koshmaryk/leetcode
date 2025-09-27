class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if not nums:
            return [-1, -1]

        def search(bad, good, p):
            while good - bad > 1:
                mid = (bad + good) // 2
                if p(mid):
                    good = mid
                else:
                    bad = mid
            return bad, good

        _, first = search(bad=-1, good=n, p=lambda x: nums[x] >= target)

        if first == n or nums[first] != target:
            return [-1, -1]

        last, _ = search(bad=-1, good=n, p=lambda x: nums[x] > target)
        return [first, last]
        