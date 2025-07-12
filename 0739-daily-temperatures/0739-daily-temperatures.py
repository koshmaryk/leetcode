class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        warmer = 0
        for curr_day in range(n - 1, -1, -1):
            curr_t = temperatures[curr_day]
            if curr_t >= warmer:
                warmer = curr_t
                continue

            days = 1
            while temperatures[curr_day + days] <= curr_t:
                days += answer[curr_day + days]
            answer[curr_day] = days
        return answer
        


# 1, 1, 4, 2, 1, 1, 0, 0
# 
# 0, 1, 2, 3, 4, 5, 6, 7
# 73,74,75,71,69,72,76,73
#
# 0, 0, 0, 0, 0, 0, 0, 0
#
# 73
# 5