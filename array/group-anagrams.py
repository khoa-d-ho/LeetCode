from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for item in strs:
            dic[item] = list(item)
            dic[item].sort()
            
        dic2 = defaultdict(list)
        for item in strs:
            dic2[tuple(dic[item])].append(item)
        
        return(list(dic2.values()))
            
