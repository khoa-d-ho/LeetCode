class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack
        stack = []
        open_count = 0
        
        for i in range(len(s)):
            if s[i] == ")": # )
                if open_count > 0:
                    stack.append(s[i])
                    open_count -= 1
                # else do nothing
            else: # letters and (
                if s[i] == "(":
                    open_count += 1
                stack.append(s[i])
        
        i = -1
        while open_count > 0:
            if stack[i] == "(":
                stack.pop(i)
                open_count -= 1
                i += 1
            i -= 1
        return "".join(stack)
            
        