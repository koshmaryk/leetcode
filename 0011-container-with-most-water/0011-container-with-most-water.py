class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_square = 0
        left, right = 0, len(height) - 1
        while (left < right):
            width = right - left
            max_square = max(max_square, width * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_square

        