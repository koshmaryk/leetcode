class Solution {
    public int rob(int[] nums) {
        int[] memo = new int[100];

        Arrays.fill(memo, -1);

        return dp(0, nums, memo);
    }

    public int dp(int i, int[] nums, int[] memo) {
        if (i >= nums.length) {
            return 0;
        }

        if (memo[i] != -1) {
            return memo[i];
        }

        return memo[i] = Math.max(dp(i + 1, nums, memo), dp(i + 2, nums, memo) + nums[i]);
    }
}