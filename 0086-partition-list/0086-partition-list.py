# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
before 2 1
after 5 3 4 3

before -> after


5,3,4,2,3,1

x=3
2,1 | 5,3,4,3

x=-1
| 5,3,4,2,3,1

"""
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_sentinel = before = ListNode(-101)
        after_sentinel = after = ListNode(-101)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next

            head = head.next

        after.next = None
        
        before.next = after_sentinel.next
        return before_sentinel.next