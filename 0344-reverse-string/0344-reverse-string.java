class Solution {
    public void reverseString(char[] s) {
        int n = s.length;
        if (n == 1) {
            return;
        }
        
        for (int i = 0; i * 2 < n; i++) {
            char temp = s[i];
            s[i] = s[n - 1 - i];
            s[n - 1 - i] = temp;
        }
    }
}