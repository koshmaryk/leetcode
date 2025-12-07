class Solution:
    '''
    length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]

    [-2,0,3,7,1,-3]

    '''
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * (length + 1)

        for i,j,inc in updates:
            diff[i] += inc
            diff[j+1] -= inc

        arr = [0] * length
        sum = 0
        for i in range(length):
            sum += diff[i]
            arr[i] = sum
        return arr
