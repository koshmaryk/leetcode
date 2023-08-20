class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            char chL = Character.toLowerCase(s.charAt(l));
            char chR = Character.toLowerCase(s.charAt(r));

            if (!Character.isLetterOrDigit(chL)) {
                l++;
            }

            if (!Character.isLetterOrDigit(chR)) {
                r--;
            }

            if (Character.isLetterOrDigit(chL) && Character.isLetterOrDigit(chR)) {
                if (chL != chR) {
                    return false;
                }

                l++;
                r--;
            }
        }

        return true;
    }
}