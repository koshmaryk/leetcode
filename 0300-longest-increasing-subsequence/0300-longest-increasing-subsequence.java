class Solution {
    public int lengthOfLIS(int[] nums) {
        int N = nums.length;
        
        int[] dp = new int[N];
        Arrays.fill(dp, 1);

        for (int i = 1; i < N; ++i) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                     dp[i] = Math.max(dp[i], 1 + dp[j]);
                }
            }
        }

        int longest = 0;
        for (int current : dp) {
            longest = Math.max(longest, current);
        }

        return longest;
    }
}