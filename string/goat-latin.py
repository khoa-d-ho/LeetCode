class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        lst = []
        lst = sentence.split(" ")
        vowels = ["u", "e", "o", "a", "i", "U", "E", "O", "A", "I"]
        for i in range(len(lst)):
            goat = "a" * (i + 1)
            # consonant
            if lst[i][0] not in vowels:
                lst[i] = lst[i][1:] + lst[i][0] + "ma"
            # vowels
            else: 
                lst[i] += "ma"
            lst[i] += goat
        
        return " ".join(lst)