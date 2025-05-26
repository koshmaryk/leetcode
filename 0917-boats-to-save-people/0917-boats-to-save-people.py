class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        #   ||
        # 1,2,2,3
        # l = 1
        # r = 1
        # boats = 2
        while l < r:
            if people[l] + people[r] > limit:
                boats += 1
                r -= 1
            else:
                boats += 1
                l += 1
                r -= 1
        return boats + 1 if l == r else boats
        