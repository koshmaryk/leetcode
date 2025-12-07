class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for first,last,seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        answer = [0] * n
        acc = 0
        for i in range(n):
            acc += diff[i]
            answer[i] = acc
        return answer
