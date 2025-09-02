class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = ""
        prev_op = "+"
        s = s + " " 

        for i in range(len(s)):
            curr_char = s[i]
            if curr_char.isdigit():
                num = num + curr_char
            # remember to have the last char check, or else the last operation won't run
            elif (not curr_char.isdigit() and curr_char != " ")or i == len(s)-1:
                if prev_op == "+":
                    stack.append(int(num))
                elif prev_op == "-":
                    stack.append(-int(num))
                elif prev_op == "*":
                    stack.append(stack.pop() * int(num))
                elif prev_op == "/":
                    stack.append(int(stack.pop() / int(num))) # cannot // to account for negative division
                prev_op = curr_char
                num = ""
        return sum(stack)

