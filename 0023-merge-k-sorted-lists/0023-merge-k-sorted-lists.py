# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i, l in enumerate(lists):
            if l:
                pq.append((l.val, i, l))

        heapq.heapify(pq)

        sentinel = curr = ListNode()
        while pq:
            _, i, l = heapq.heappop(pq)
            curr.next = l
            curr = curr.next

            if l.next:
                heapq.heappush(pq, (l.next.val, i, l.next))
        return sentinel.next