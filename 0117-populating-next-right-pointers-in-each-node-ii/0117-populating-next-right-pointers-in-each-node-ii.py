"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

root->null

leftmost = root
                
          1
x->   2       3 

   4     5   6   7


1
x->2->3->

3
x->4->5->6->7->

4
x->


"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        leftmost = root
        while leftmost:
            curr = leftmost
            sentinel = tail = Node()
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            
            leftmost = sentinel.next # 2, 4
        return root
