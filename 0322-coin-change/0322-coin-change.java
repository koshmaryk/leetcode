class Solution {
    public int coinChange(int[] coins, int amount) {
        return change(coins, amount, new int[amount + 1]);
    }

    public int change(int[] coins, int value, int[] memo) {
        if (value < 0) return -1;
        if (value == 0) return 0;
        if (memo[value] != 0) return memo[value];

        int min = Integer.MAX_VALUE;
        for (int i = 0; i < coins.length; ++i) {
            int ans = change(coins, value - coins[i], memo);
            if (ans >= 0 && ans < min) {
                min = 1 + ans;
            }
        }

        return memo[value] = min == Integer.MAX_VALUE ? -1 : min;
    }
}