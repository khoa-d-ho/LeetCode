class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack: 75 71 69 
        # decreasing monotonic stack
        # while [-1] value smaller than current value:
            # pop
            # index value being popped += 1
            # index corresponds to remaining value in the stack += 1


        res = [0] * len(temperatures)
        stack = []
        threshold = 0
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                curr = stack.pop()
                res[curr[-1]] += i - curr[-1]
            stack.append((temperatures[i], i))
        return res
                
                


            