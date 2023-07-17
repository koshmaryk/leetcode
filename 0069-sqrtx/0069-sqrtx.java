class Solution {
    public int mySqrt(int x) {
        double bad = 0;
        double good = x;
        while (good - bad > 0.00001) {
            double mid = bad + (good - bad) / 2;
            if (mid * mid >= x) {
                good = mid;
            } else {
                bad = mid;
            }
        }
        
        return (int) good;
    }
}