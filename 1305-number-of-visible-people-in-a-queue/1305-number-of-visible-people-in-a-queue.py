class Solution:
    '''
    3,2,1,2,1,2,1,1,0

    10,6,4,3,8,5,11,9

    11,10

    '''
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)

        answer = [0] * n

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] < heights[i]: # e.g. 9 < 11
                stack.pop()
                # person at i position sees one person that was popped
                answer[i] += 1

            if stack:
                answer[i] += 1

            stack.append(i)

        return answer
