class Solution:
    '''
    4,3,2,1
    0,1,2,3

    0,1,2,3

    4,2,3,1
    0,2,3

    4,3,1

    1,2,3,4
    3


    '''
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = [] # 1,3,4

        stack = [] # 4
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()

            if not stack:
                answer.append(i)

            stack.append(i)

        return answer[::-1]