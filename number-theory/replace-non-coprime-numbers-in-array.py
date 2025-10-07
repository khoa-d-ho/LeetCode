class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = [] 
        for item in nums: 
            curr = item
            while stack:
                if gcd(stack[-1], curr) == 1:	
                    break
                curr  = lcm(stack.pop(), curr)
            stack.append(curr)
        return stack 
