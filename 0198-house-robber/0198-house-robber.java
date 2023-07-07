class Solution {
    public int rob(int[] nums) {
        int N = nums.length;
        int[] max = new int[N + 1];

        max[N] = 0;
        max[N - 1] = nums[N - 1];

        for (int i = N - 2; i >= 0; --i) {
            max[i] = Math.max(max[i + 1], max[i + 2] + nums[i]);
        }

        return max[0];
    }
}