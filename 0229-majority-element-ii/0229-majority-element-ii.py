from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        output = []
        for num, count in freq.items():
            if count > len(nums) // 3:
                output.append(num)
        return output
