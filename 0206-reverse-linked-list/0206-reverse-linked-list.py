# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
head = 1
newHead = reverseList(2->3)

    head = 2
    newHead = reverseList(3)

        head = 3
        newHead = 3
        return 3

    head.next.next = 3->2
    head.next = None 2->None
    return 3 #


head.next.next = 2->1
head.next = 1->None
return 3


"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
