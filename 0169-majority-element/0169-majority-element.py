class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        candidate = 0
        counter = 0
        for key, value in freq.items():
            if value > counter:
                candidate = key
                counter = value
        return candidate
        