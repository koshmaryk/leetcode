class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def non_descreasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False
            return True

        def find_next_pair(arr):
            min_sum = float('inf')
            target_index = -1
            for i in range(len(arr) - 1):
                curr_sum = arr[i] + arr[i + 1]
                if curr_sum < min_sum:
                    min_sum = curr_sum
                    target_index = i
            return min_sum, target_index

        ops = 0
        while not non_descreasing(nums):
            min_sum, target_index = find_next_pair(nums)
            nums[target_index] = min_sum
            nums.pop(target_index + 1)
            ops += 1
        return ops