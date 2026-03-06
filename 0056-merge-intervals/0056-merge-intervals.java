class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (i0, i1) -> Integer.compare(i0[0], i1[0]));

        var merged = new ArrayList<int[]>();
        for (int[] interval: intervals) {
            if (merged.isEmpty() || merged.getLast()[1] < interval[0]) {
                merged.add(interval);
            } else {
                merged.getLast()[1] = Math.max(merged.getLast()[1], interval[1]);
            }
        }
        
        return merged.toArray(new int[merged.size()][2]);
    }
}