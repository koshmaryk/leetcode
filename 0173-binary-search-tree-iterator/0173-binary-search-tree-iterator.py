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


stack = 4 6 2

p = 2



LRC

'''
# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.stack = 

#     def next(self) -> int:
#         if not self.hasNext():
#             return -1


        
#     def hasNext(self) -> bool:
#         if self.stack:
#             return True
#         return False

# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.p = root
#         self.stack = []
        

#     def next(self) -> int:
#         if not self.hasNext():
#             return -1

#         while self.p:
#             self.stack.append(self.p)
#             self.p = self.p.left

#         self.p = self.stack.pop()
#         val = self.p.val
#         self.p = self.p.right
#         return val
        

#     def hasNext(self) -> bool:
#         if self.stack or self.p:
#             return True
#         return False

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [(root, False)] if root else []

    def next(self) -> int:
        if not self.hasNext():
            return -1

        while self.stack:
            node, visited = self.stack.pop()
            if visited:
                return node.val
            if node.right:
                self.stack.append((node.right, False))
            self.stack.append((node, True))
            if node.left:
                self.stack.append((node.left, False))
        
    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False

# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.stack = [root]

#     def next(self) -> int:
#         if not self.hasNext():
#             return -1

#         ptr = self.stack.pop()
#         val = ptr.val

#         if ptr.right:
#             self.stack.append(ptr.right)
#         if ptr.left:
#             self.stack.append(ptr.left)

#         return val
        
#     def hasNext(self) -> bool:
#         if self.stack:
#             return True
#         return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()