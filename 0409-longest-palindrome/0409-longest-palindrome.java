class Solution {
    public int longestPalindrome(String s) {
        int[] count = new int[128];
        for (char c : s.toCharArray()) {
            count[c]++;
        }
      
        int ans = 0;
        for (int i = 0; i < count.length; ++i) {
            if (count[i] > 0) {
        	    ans += count[i] / 2 * 2; // 5
                if (ans % 2 == 0 && count[i] % 2 == 1) { // false && true
                    ans += 1;
                }
            }
        }

        return ans;
    }
}