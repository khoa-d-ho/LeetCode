class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        left = 0
        max_length = 0
        counter = 1
        for right in range(1, len(word)):
            if word[right] < word[right - 1]:
                left = right
                counter = 1

            if word[right] > word[right - 1]:
                counter += 1

            if counter == 5:
                max_length = max(max_length, right - left + 1)
        
        return max_length