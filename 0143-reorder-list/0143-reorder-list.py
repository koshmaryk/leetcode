# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        q = deque()
        curr = head
        while curr:
            q.append(curr)
            curr = curr.next
        
        curr = q.popleft()
        i = 1
        while q:
            curr.next = q.popleft() if i % 2 == 0 else q.pop()
            curr = curr.next
            i += 1

        curr.next = None