class Solution {
    public int[] twoSum(int[] nums, int target) {
        var seen = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            var diff = target - nums[i];
            if (seen.containsKey(diff)) {
                return new int[]{seen.get(diff), i};
            }

            seen.put(nums[i], i);
        }
        
        return new int[]{-1, -1};
    }
}