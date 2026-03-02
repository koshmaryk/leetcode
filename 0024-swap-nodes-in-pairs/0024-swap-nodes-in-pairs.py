# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""


1,2,3,4


1st = 1
2nd = 2

1st.next = 2nd.next
1.next -> 3
2nd.next = 1st
2.next -> 1

2,1,3,4



dummy
dummy.next = head

prev = dummy

head and head.next

1st = head
2nd = head.next

swap

prev.next = 2nd
prev = 1st



dummy.next

"""
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-1)
        sentinel.next = head

        prev = sentinel
        while head and head.next:
            odd = head
            even = head.next

            odd.next = even.next
            even.next = odd

            prev.next = even
            prev = odd
            head = odd.next

        return sentinel.next
        