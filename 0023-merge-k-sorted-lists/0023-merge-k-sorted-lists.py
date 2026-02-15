# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
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

            curr.next = l1 if l1 else l2

            return sentinel.next

        def mergeHelper(l, r):
            if r - l < 2:
                return lists[l]

            mid = (l + r) // 2

            left = mergeHelper(l, mid)
            right = mergeHelper(mid, r)

            return merge(left, right)

        if not lists:
            return None

        return mergeHelper(0, len(lists))