class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        w = s.split()
        return " ".join(reversed(w))
            