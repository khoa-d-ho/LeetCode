class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        count = 0
        i = 0
        while i < len(abbr):
            if abbr[i] == "0" or count >= len(word):
                return False

            number = ""
            # edge case "12", i can go inf
            while i < len(abbr) and abbr[i].isdigit():
                number += abbr[i]
                i += 1
            
            if number:
                count += int(number)
            else: 
                if abbr[i] != word[count]:
                    return False
                i += 1
                count += 1
            
        return count == len(word)

        