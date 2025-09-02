class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = "" # output
        current = "" # letter being checked atm
        pos = 0
        status = True
        if len(strs) == 0 or "" in strs:
            return ""
        # stop recording pos when reach end of shortest string
        while status == True and pos < len(min(strs, key=len)):
            current = strs[0][pos]
            for item in strs:
                if item[pos] != current:
                    status = False
                    break
            if status == True:
                common += current
                pos += 1
        return common

        


        