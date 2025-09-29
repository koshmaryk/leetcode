"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    '''
    40/5
    30 10 20
    '''
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        prev, curr = head, head.next
        while True:
            if prev.val <= insertVal <= curr.val:
                prev.next = Node(insertVal, curr)
                return head

            if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                prev.next = Node(insertVal, curr)
                return head

            prev, curr = curr, curr.next

            if prev == head:
                break

        prev.next = Node(insertVal, curr)
        return head
        