# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        p1 = head # 1
        p2 = sentinel

        while n > 0: # 2; 1; 0
            p1 = p1.next # 2; 3
            n -= 1

        while p1:
            p1 = p1.next # 4; 5; None
            p2 = p2.next # 1; 2; 3

        p2.next = p2.next.next
        return sentinel.next