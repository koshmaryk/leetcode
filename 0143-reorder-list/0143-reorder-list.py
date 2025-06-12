# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1,2,3,4,5
        slow = fast = head # 1; 1 | 2; 3 | 3;5
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next # 4
        prev = slow.next = None # don't forget to remove link between l1 and l2
        while curr:
            tmp = curr.next # 5 | None
            curr.next = prev # None <- 4 | None <- 4 <- 5
            prev = curr # 4 | 5
            curr = tmp # 5 | None

        # l1 = 1,2,3
        # l2 = 5, 4
        l1, l2 = head, prev
        while l2:
            tmp1, tmp2 = l1.next, l2.next # 2,3; 4 | 3, None
            l1.next = l2 # 1 -> 5,4 | .. 2 -> 4
            l2.next = tmp1 # 5 -> 2,3 | .. 4 -> 3
            l1, l2 = tmp1, tmp2 # 2,3; 4 | 3, None

        