"""
1 2 3
x y z 
4 5 6
7 8 9

go right to the end 
go down to the end
go left to the end
go up to the end

up=0
left=0
down=ROWS-1
right=COLS-1

while len(ans) < m * n
left to right+1
up+1 to down+1
right-1 to left-1
down-1 to up-1

"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = n - 1
        up = 0
        down = m - 1
        ans = []
        """
        1 2 3
        x y z 
        4 5 6
        7 8 9
        """
        while len(ans) < m * n:
            for c in range(left, right + 1):
                ans.append(matrix[up][c])

            for r in range(up + 1, down + 1):
                ans.append(matrix[r][right])

            if up != down:
                for c in range(right - 1, left - 1, - 1):
                    ans.append(matrix[down][c])

            if left != right:
                for r in range(down - 1, up, - 1):
                    ans.append(matrix[r][left])

            left += 1
            right -= 1
            up += 1
            down -= 1
        return ans
