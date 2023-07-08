class Solution {
    public int rob(int[] nums) {
        int N = nums.length;
        if (N == 1) return nums[0];
        return Math.max(helper(nums, 0, N - 1), helper(nums, 1, N));
    }

    public int helper(int[] nums, int start, int stop) {
        int current = 0, next = 0;
        for (int i = start; i < stop; ++i) {
            int max = Math.max(current + nums[i], next);
            current = next;
            next = max;
        }

        return next;
    }
}