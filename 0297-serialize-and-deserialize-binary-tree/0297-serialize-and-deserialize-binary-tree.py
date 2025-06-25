# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        if not root:
            return "nil"

        preorder = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                preorder.append("nil")
                continue

            preorder.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ",".join(preorder)
        

    def deserialize(self, data):
        if data == "nil":
            return None

        preorder = data.split(",")
        root = TreeNode(int(preorder[0]))
        queue = deque([root])
        index = 1
        while queue:
            curr = queue.popleft()

            if preorder[index] != "nil":
                curr.left = TreeNode(int(preorder[index]))
                queue.append(curr.left)
            index += 1

            if preorder[index] != "nil":
                curr.right = TreeNode(int(preorder[index]))
                queue.append(curr.right)
            index += 1

        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))