# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""

1->2->3 

None<-1 | 2->3->None
prev      curr

None<-1<-2 | 3->None
prev         curr

None<-1<-2<-3 | None
prev           curr

prev = next = None
curr = head # 1

next = curr.next # 2->3; 
curr.next = prev # 1->None;
prev = curr # 1
curr = next # 2->3



"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = next = None
        curr = head
        while curr:
            next = curr.next # 2
            curr.next = prev # None<-1
            prev = curr # 1
            curr = next # 2->3
        return prev
    