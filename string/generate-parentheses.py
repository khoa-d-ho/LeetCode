class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, o, c):
            if len(curr) == n * 2:
                res.append(curr)
            
            if o < n:
                curr += "("
                backtrack(curr, o + 1, c)
                curr = curr[:len(curr) - 1]

            if c < o:
                curr += ")"
                backtrack(curr, o, c + 1)
                curr = curr[:len(curr) - 1]
                
        backtrack("", 0, 0)
        return res