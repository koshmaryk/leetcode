class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> counters = new HashMap<>();
        for (char ch : s.toCharArray()) {
            counters.put(ch, counters.getOrDefault(ch, 0) + 1);
        }

        for (int i = 0; i < s.length(); ++i) {
            if (counters.get(s.charAt(i)) == 1) {
                return i;
            }
        }

        return -1;
    }
}