# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for head in lists:
            curr = head
            while curr:
                values.append(curr.val)
                curr = curr.next

        # 1,1,2,3,4,4,5,6
        values.sort()

        sentinel = ListNode()
        curr = sentinel
        for val in values: # 1;1;2
            curr.next = ListNode(val)
            curr = curr.next # 1;1

        # 1->1->2
        return sentinel.next