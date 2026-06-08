class Solution:
    '''
    bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5

    [10,45,-10,-20,0,-25]
   0 1  2   3   4  5  6

    25
    [10,55,45,25,25]

    '''
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        answer = [0] * n
        p = 0
        for i in range(n):
            p += diff[i]
            answer[i] = p
        return answer
