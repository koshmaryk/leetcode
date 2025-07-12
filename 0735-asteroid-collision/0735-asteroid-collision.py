class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            exploded = False
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = stack[-1] + asteroid
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    exploded = True
                    break
                else:
                    exploded = True
                    stack.pop()
                    break
                    
            if not exploded:        
                stack.append(asteroid)
                
        return stack


        # 10 2 -5
        # 
        # 10 -5