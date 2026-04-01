class Solution:
    '''
    

    '''
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []

        max_height = 0
        for i in range(n - 1, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                answer.append(i)
        return answer[::-1]