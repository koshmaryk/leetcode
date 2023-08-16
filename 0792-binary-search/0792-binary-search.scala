object Solution {
    def search(nums: Array[Int], target: Int): Int = {
        val n = nums.length
        var bad = -1
        var good = n
        while (good - bad > 1) {
            val mid = bad + (good - bad) / 2
            if (nums(mid) >= target) good = mid
            else bad = mid
        }

        if (good == n || nums(good) != target) -1
        else good
    }
}