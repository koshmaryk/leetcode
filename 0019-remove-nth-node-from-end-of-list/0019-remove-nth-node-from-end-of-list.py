# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0 # 5
        curr = head
        while curr:
            size += 1
            curr = curr.next

        sentinel = ListNode()
        sentinel.next = head
        curr = sentinel
        while size - n > 0: #  5 - 2 > 0; 4 - 2 > 0; 3 - 2 > 0; 2 - 2 > 0; 
            size -= 1 # 4; 3; 2
            curr = curr.next # 2; 3; 4

        curr.next = curr.next.next
        return sentinel.next