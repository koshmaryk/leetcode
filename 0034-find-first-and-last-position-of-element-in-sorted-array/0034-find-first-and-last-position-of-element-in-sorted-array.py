class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        def bisect(arr, p):
            bad, good = -1, len(arr)
            while good - bad > 1:
                mid = (bad + good) // 2
                if p(mid):
                    good = mid
                else:
                    bad = mid
            return bad, good


        _, first = bisect(arr=nums, p=lambda x: nums[x] >= target)
        last, _ = bisect(arr=nums, p=lambda x: nums[x] > target)
        if first > last:
            return [-1, -1]
        return [first, last]



        