class Solution:
    # 0 1 2 3 4 5
    #   |   |
    # 1 2 3 1 2 3
    # k = 2
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        seen = {}

        l = 0
        seen[nums[l]] = 1
        for r in range(1, len(nums)):
            seen[nums[r]] = seen.get(nums[r], 0) + 1
            while l < r and r - l > k:
                seen[nums[l]] -= 1
                l += 1
            if seen[nums[r]] == 2:
                return True
        return False