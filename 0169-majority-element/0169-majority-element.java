class Solution {
    public int majorityElement(int[] nums) {
        int counter = 0;
        int current = 0;
        for (int i = 0; i < nums.length; ++i) {
          if (counter == 0) {
            current = nums[i];
            counter++;
          } else if (nums[i] == current) {
            counter++;
          } else {
            counter--;
          }
        }

        return current;
    }
}