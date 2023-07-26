class Solution {
    public int search(int[] nums, int target) {
        int bad = -1;
        int good = nums.length;
        while (good - bad > 1) {
            int mid = (bad + good) / 2;
            if (nums[mid] >= target) {
                good = mid;
            } else {
                bad = mid;
            }
        }
        
        if (good == nums.length || nums[good] != target) return -1;
        else return good;
        
    }
}