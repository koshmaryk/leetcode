class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0) return new ArrayList<>();

        var groups = new HashMap<String, List<String>>();
        for (String s: strs) {
            char[] chs = s.toCharArray();
            Arrays.sort(chs);
            var key = String.valueOf(chs);
            if (!groups.containsKey(key)) groups.put(key, new ArrayList<>());
            groups.get(key).add(s);
        }

        return new ArrayList<>(groups.values());
    }
}