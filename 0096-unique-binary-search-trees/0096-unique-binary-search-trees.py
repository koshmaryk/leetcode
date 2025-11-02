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
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                # root=2, left=2-1, right=5-2
                dp[nodes] += dp[root - 1] * dp[nodes - root]
        return dp[n]
        