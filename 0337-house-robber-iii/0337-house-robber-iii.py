# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
     1                
    / \   
   2   3 
  /\   /\ 
 4  5 6  7

               [23, 22]                
             /        \   
          [2,9]      [3,13] 
        /    \       /     \ 
      [4,0] [5,0]  [6,0] [7,0]

  [0,0] [0,0] [0,0] [0,0] [0,0] [0,0]

         4
        /
       1
      /
     2
    /
   3 

         [7,4]
        /
       [4,3
      /
     [2,3]
    /
   [3,0]
  /
 [0,0] 
'''
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if not node:
                return (0, 0) # (rob, not_rob)

            left_rob, left_not_rob = helper(node.left)
            right_rob, right_not_rob = helper(node.right)

            rob_curr = node.val + left_not_rob + right_not_rob
            not_rob_curr = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
            return (rob_curr, not_rob_curr)
        
        rob, not_rob = helper(root)
        return max(rob, not_rob)