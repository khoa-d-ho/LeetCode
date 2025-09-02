class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            temp = 0
            if s[i] != "0":
                temp = one_back
            twos = int(s[i - 1:i + 1])
            if twos >= 10 and twos <= 26:
                temp += two_back

            two_back = one_back
            one_back = temp

        return one_back
        
        