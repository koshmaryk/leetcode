# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
'''
           7
        /     \ 
    4           10
   / \         /   \
  2   6       8     12 
/ \   /        \    /  \  
1  3  5         9  11  13

Case 1 & 2
           7
        /     \ 
    4           10
   / \         /   \
  2   5       9     12 
/ \                /  \  
1  3              11  13

Case 3
           7
      /        \ 
                10
     \         /   \
      6       8     12 
      /        \    /  \  
      5         9  11  13
     /
    2
   /\
  1  3
'''

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(root):
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                right = root.right # 6
                left = root.left # 2
                # find smallest in right subtree, 4 successor = 5
                while right.left: 
                    right = right.left # 5
                right.left = left # 5.left = 2
                return root.right # 6

        if not root:
            return None

        if root.val == key:
            return helper(root)

        curr = root
        while curr:
            if key < curr.val:
                if curr.left and curr.left.val == key:
                    curr.left = helper(curr.left) # 7.left = 5
                    break
                curr = curr.left
            else:
                if curr.right and curr.right.val == key:
                    curr.right = helper(curr.right)
                    break
                curr = curr.right
        return root
        