class Solution:
    '''
    4,3,2,1
    0,1,2,3

    4,2,3,1
    0,2,3

    1,2,3,4
    3


    '''
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)

        stack = [] # 0,2,3
        for i in range(n):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()

            stack.append(i)

        return stack