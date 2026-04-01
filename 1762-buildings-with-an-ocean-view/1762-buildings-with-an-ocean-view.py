class Solution:
    '''
    

    '''
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []

        for i in range(n):
            while answer and heights[answer[-1]] <= heights[i]:
                answer.pop()
            answer.append(i)
        return answer