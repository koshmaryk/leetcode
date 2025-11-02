class Solution:
    '''
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3]

    1,2,3,4,5
    
    1   2   3,4,5

    1; 1->2, 2->1; 3->2->1; 1<-3->2, 1->2->3, 2->3->1, 2->1->3
    '''
    def numTrees(self, n: int) -> int:
        memo = {}
        def count(leftmost, rightmost):
            if leftmost >= rightmost:
                return 1

            if (leftmost, rightmost) in memo:
                return memo[(leftmost, rightmost)]

            cnt = 0
            for root in range(leftmost, rightmost + 1):
                left = count(leftmost, root - 1)
                right = count(root + 1, rightmost)
                cnt += left * right

            memo[(leftmost, rightmost)] = cnt
            return memo[(leftmost, rightmost)]


        return count(1, n)
        