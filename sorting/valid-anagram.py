class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict = {}
        
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1

        for i in t:
            if i in dict:
                dict[i] -= 1
                if dict[i] < 0:
                    return False
            else: 
                return False
        
        return True