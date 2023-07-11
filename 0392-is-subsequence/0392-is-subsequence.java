class Solution {
    public boolean isSubsequence(String s, String t) {
        return isSubsequence(s, t, 0, 0);
    }

    public boolean isSubsequence(String s, String t, int left, int right) {
        if (left == s.length()) {
            return true;
        }

        if (right == t.length()) {
            return false;
        }

        if (s.charAt(left) == t.charAt(right)) {
            left++;
        }

        right++;

        return isSubsequence(s, t, left, right);
    }
}