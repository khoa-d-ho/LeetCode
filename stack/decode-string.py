class Solution:
    def decodeString(self, s: str) -> str:
        string_stack  = []
        count_stack = []
        curr_str = ""
        k = 0
        for c in s:
            if c.isdigit():
                k = k* 10 + int(c)
            elif c == "[":
                count_stack.append(k)
                string_stack.append(curr_str)
                curr_str = ""
                k = 0
            elif  c == "]":
                decoded_str = string_stack.pop()  + curr_str * count_stack.pop()
                curr_str = decoded_str
            else:
                curr_str += c
        return curr_str
                