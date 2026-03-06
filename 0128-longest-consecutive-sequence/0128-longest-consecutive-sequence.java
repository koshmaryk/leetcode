class Solution {
    public int longestConsecutive(int[] nums) {
        var s = new HashSet<Integer>();
        for (int num: nums) {
            s.add(num);
        }

        var ans = 0;
        for (int num: s) {
            if (!s.contains(num - 1)) {
                var curr_length = 0;
                while (s.contains(num + curr_length)) {
                    curr_length++;
                }
                ans = Math.max(ans, curr_length);
            }
        }

        return ans;
    }
}
