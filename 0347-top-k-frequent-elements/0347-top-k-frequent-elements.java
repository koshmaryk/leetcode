class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        var counter = new HashMap<Integer, Integer>();
        for (int num: nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        var buckets = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < nums.length + 1; i++) {
            buckets.add(new ArrayList<Integer>());
        } 

        for (Map.Entry<Integer, Integer> entry: counter.entrySet()) {
            buckets.get(entry.getValue()).add(entry.getKey());
        }

        var topK = new int[k];
        var idx = 0;
        for (int i = nums.length; i >= 0; i--) {
            var bucket = buckets.get(i);
            for (int num: bucket) {
                topK[idx++] = num;
                if (idx == k) {
                    return topK;
                }
            }
        }

        return topK;
    }
}