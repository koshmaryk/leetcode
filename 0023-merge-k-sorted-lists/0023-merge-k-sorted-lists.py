# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]):
            sentinel = ListNode()
            curr = sentinel
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            if l1 or l2:
                curr.next = l1 if l1 else l2
            
            return sentinel.next

        if not lists:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i - 1], lists[i])

        return lists[-1]