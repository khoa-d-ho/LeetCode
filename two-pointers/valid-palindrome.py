class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        while front <= back: 
            # iterate until both are letters to compare 
            if s[front].isalpha() == False and s[front].isnumeric() == False:
                front += 1
            elif s[back].isalpha() == False and s[back].isnumeric() == False:
                back -= 1
            else:
                if s[front].lower() != s[back].lower():
                    return False
                front += 1
                back -= 1
        return True