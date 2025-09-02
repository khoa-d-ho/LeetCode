class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        i = 0
        roman_dict = {'M' : 1000, 'CM' : 900, 'D' : 500, 'CD' : 400, 'C' : 100, 'XC' : 90, 'L' : 50, 'XL' : 40, 'X' : 10, 'IX' : 9, 'V' : 5, 'IV' : 4, 'I' : 1}
        while i < len(s):
            if i < len(s) - 1 and s[i:i+2] in roman_dict:
                value += roman_dict[s[i:i+2]] 
                i += 2

            else: 
                value += roman_dict[s[i]] 
                i += 1   

        return value 
            
        