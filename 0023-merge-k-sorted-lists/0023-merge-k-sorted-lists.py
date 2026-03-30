# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""


[1,4,5],[1,3,4],[2,6]

1->1->3->4->4->5

1->1->2->3->4->4->5->6

"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            sentinel = curr = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            curr.next = l1 if l1 else l2

            return sentinel.next

        if not lists:
            return None

        n = len(lists)
        for i in range(1, n):
            lists[i] = merge(lists[i - 1], lists[i])
        return lists[-1]