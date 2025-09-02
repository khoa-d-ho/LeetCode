class Solution:
    def clearStars(self, s: str) -> str:
        s_list = list(s)
        l = []
        for i in range(26):
            l.append([])

        for i in range(len(s)):
            if s[i] != "*":
                letter_num = ord(s[i]) - ord("a")
                l[letter_num].append(i)
            else:
                for lst in l:
                    if lst:
                        idx = lst.pop()
                        s_list[idx] = "*"
                        break

        res = []
        for item in s_list:
            if item != "*":
                res.append(item)
        res = "".join(res)
        return res