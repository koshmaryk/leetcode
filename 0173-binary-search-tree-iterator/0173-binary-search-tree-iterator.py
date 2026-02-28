# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
            4
        2       6
    1   3      5    7


        4
    2
1      3


[]

p = 

7
'''
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.p = root
        self.stack = []
        

    def next(self) -> int:
        if not self.hasNext():
            return -1

        while self.p:
            self.stack.append(self.p)
            self.p = self.p.left

        self.p = self.stack.pop()
        val = self.p.val
        self.p = self.p.right
        return val
        

    def hasNext(self) -> bool:
        if self.stack or self.p:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()