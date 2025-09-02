class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        i = 0
        j = 0
        while i <= len(s):
            if i == len(s):
                return True
            while j <= len(t):
                if j == len(t):
                    return False
                else:
                    if t[j] == s[i]:
                        i += 1
                        j += 1
                        break
                    else: 
                        j += 1

        return False





        