class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        def collision_check(a):
            if stack:
                # asteroid is moving left while the old asteroid is moving right
                # meaning they will collide
                if a < 0 < stack[-1]:
                    
                    # equal size collision
                    if a + stack[-1] == 0:
                        stack.pop()

                    # new asteroid breaks old asteroid, recurse to check for more collisions
                    elif a + stack[-1] < 0:
                        stack.pop()
                        collision_check(a)

                # no collision, add asteroid
                else: stack.append(a)            
            
            # empty stack, add asteroid
            else:
                stack.append(a)
                   

        for a in asteroids:
            collision_check(a)

        return stack
                
            