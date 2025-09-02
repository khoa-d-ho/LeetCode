class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            flag = True
            while (stack) and (stack[-1] > 0) and a < 0:
                if abs(stack[-1]) < abs(a):
                    stack.pop()
                    continue
            
                elif abs(stack[-1]) == abs(a):
                    stack.pop()
                flag = False
                break

            if flag:
                stack.append(a)
        return stack    
