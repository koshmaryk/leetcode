class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 3 * (n/3 + 1) = n + 3
        n = len(nums)
        candidate1 = candidate2 = float('inf')
        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        output = []
        if count1 > n // 3:
            output.append(candidate1)
        if count2 > n // 3:
            output.append(candidate2)
        return output
