/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int bad = 0;
        int good = n;
        while (good - bad > 1) {
            int mid = bad + (good - bad) / 2;
            if (isBadVersion(mid)) {
                good = mid;
            } else {
                bad = mid;
            }
        }
        
        return good;
    }
}