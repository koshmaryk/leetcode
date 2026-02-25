# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''

    [4,2,5,1,3], target = 2.2

    4 -> 1.8
    5 -> 2.8


    [4,2,5,1,3], target = 1.5

    diff = 2.5; 0.5; 0.5
    closest = 4; 2; 1

    '''
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root
        curr = root

        while curr:
            if abs(curr.val - target) < abs(closest.val - target) or (abs(curr.val - target) == abs(closest.val - target) and curr.val < closest.val):
                closest = curr

            if target < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return closest.val
        