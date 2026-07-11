# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next

        prev = None
        curr = head
        # 1 2 3 4 5 6 7
        for _ in range(k):
            next = curr.next # 2->3; 3->4; 4
            curr.next = prev # 1->4; 2->1->4; 3->2->1->4
            prev = curr # 1; 2; 3
            curr = next # 2; 3; 4

        
        head.next = self.reverseKGroup(curr, k) # 4->5->6->7, 3
        return prev
