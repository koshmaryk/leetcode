"""

[2,2,-1,2,2,2]

"""
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = defaultdict(list)
        for employee, mgr in enumerate(manager):
            if mgr != -1:
                subs[mgr].append(employee)

        def dfs(employee):
            max_time = 0
            for sub in subs[employee]:
                max_time = max(max_time, dfs(sub))
            return informTime[employee] + max_time

        return dfs(headID)