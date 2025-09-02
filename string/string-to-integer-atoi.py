class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: 
            return 0
        i = 0
        sign = 0
        res = 0

        if s[0] == "-":
            sign = -1
            i = 1
        elif s[0] == "+":
            i = 1
        else: 
            i = 0
        
        while i < len(s):
            if s[i].isdigit():
                res = res * 10 + (ord(s[i]) - ord('0'))

                i += 1
            else: 
                break
        if sign == -1:
            res = res * (-1)
        
        if res > 2**31 - 1:
            res = 2**31 - 1
        elif res < -(2**31):
            res = -(2**31)

        return res