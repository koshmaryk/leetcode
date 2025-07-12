class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for curr_day, curr_t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < curr_t:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return answer
        
# 1, 1, 4, 2, 1, 1, 0, 0
# 
# 0, 1, 2, 3, 4, 5, 6, 7
# 73,74,75,71,69,72,76,73
#
# 1, 1, 4, 2, 1, 1, 0, 0
#
#
# stack = [6,7]
# 