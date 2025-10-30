"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


                
              1
x ->      2       3  
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        leftmost = root # 1
        while leftmost:
            curr = leftmost # 1 | 2 
            sentinel = tail = Node(-101) # x->2->3-> | x->4->5->7->
            while curr: # 3
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            leftmost = sentinel.next # 2 | 4
        return root
