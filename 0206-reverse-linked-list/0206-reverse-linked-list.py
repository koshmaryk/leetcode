# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1,2,3

head 1
newHead = reverse(2->3)

    head = 2
    newHead = reverse(3)

        head = 3
        newHead = 3
        return 3
    
    head.next.next = head # 3->2
    head.next = None # 2->
    return 3

head.next.next = head # 2->1
head.next = None # 1->
return 3

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return newHead # 3->2->1
        