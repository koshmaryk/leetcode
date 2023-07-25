class Solution {
    public int findJudge(int n, int[][] trust) {
        if (trust.length < n - 1) {
            return -1;
        }
        
        int[] scores = new int[n + 1];
        for (int[] edge : trust) {
            scores[edge[0]]--;
            scores[edge[1]]++;
        }
        
        for (int i = 1; i < n + 1; ++i) {
            if (scores[i] == n - 1) {
                return i;
            }
        }
        
        return -1;
    }
}