class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window_len = len(p) 
        i = 0
        dic = {}
        res = []
        default = Counter(p) 
        current = Counter()
        while i < len(s):
            current[s[i]] += 1
            if i >= len(p):
                if current[s[i - window_len]] != 0:
                    current[s[i - window_len]] -= 1   
                else:
                    del current[s[i - window_len]] 

            if current == default:
                res.append(i - window_len + 1)
            i += 1
        return res
