# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        rand = 0
        while True:
            row, col = rand7(), rand7()
            rand = 7 * (row - 1) + col
            if rand <= 40:
                break
        return (rand - 1) % 10 + 1
