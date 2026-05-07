"""

[2,2,-1,2,2,2]

"""
from collections import defaultdict, deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = defaultdict(list)
        for employee, mgr in enumerate(manager):
            if mgr != -1:
                subs[mgr].append(employee)

        ans = 0
        queue = deque([(headID, 0)])
        while queue:
            employee, t = queue.popleft()
            t += informTime[employee]
            ans = max(ans, t)

            for sub in subs[employee]:
                queue.append((sub, t))
        return ans