class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, curr = 0, 0
        s = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]

            if curr < 0:
                curr = 0
                s = i + 1
        return s if total >= 0 else -1
        