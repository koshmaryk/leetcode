class Solution:
    # 
    # 
    # 0 1 0 2 1 0 1 3 2 1 2 1
    # 
    def trap(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        while l < r:
            # the water level at position l is determined by lmax
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                # there's definitely a wall on the right side, rmax >= lmax
                ans += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                # there's definitely a wall on the left side, lmax >= rmax
                ans += rmax - height[r]
        return ans