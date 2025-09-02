class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        map1 = {}
        map2 = {}

        for c in word1:
            if c in map1:
                map1[c] += 1
            else:
                map1[c] = 1
        
        for c in word2:
            if c in map2:
                map2[c] += 1
            else:
                map2[c] = 1
        key1 = sorted(list(map1.keys()))
        key2 = sorted(list(map2.keys()))
        if not (key1 == key2):
            return False

        value1 = list(map1.values())        
        value2 = list(map2.values()) 
        value1.sort()
        value2.sort()

        return value1 == value2       