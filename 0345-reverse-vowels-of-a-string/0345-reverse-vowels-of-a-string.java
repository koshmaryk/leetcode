class Solution {
    public String reverseVowels(String s) {
        char[] chs = s.toCharArray();
        int left = 0;
        int right = chs.length - 1;
        while (left < right) {
            if (isVowel(chs[left]) && isVowel(chs[right])) {
                char temp = chs[left];
                chs[left] = chs[right];
                chs[right] = temp;
                left++;
                right--;
            }
            
            if (!isVowel(chs[left])) {
                left++;
            }
            
            if (!isVowel(chs[right])) {
                right--;
            } 
        }
        
        return String.valueOf(chs);
    }
    
     private boolean isVowel(char ch) {
        return 'a' == ch || 'e' == ch || 'i' == ch || 'o' == ch || 'u' == ch || 'A' == ch || 'E' == ch || 'I' == ch || 'O' == ch || 'U' == ch;
    }
}