class Solution:
    def isValid(self, s: str) -> bool:
        ref = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        brackets = []
        if s[0] in ref or s == "":
            return False

        for b in s:
            if b == "(" or b == "[" or b == "{":
                brackets.append(b)
            else:
                if len(brackets) == 0 or ref[b] != brackets[-1]:
                    return False
                else: 
                    brackets.pop(-1)

        if len(brackets) != 0:
            return False
        return True
