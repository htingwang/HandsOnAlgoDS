class Solution:
    def calculate(self, s: str) -> int:
        num = ans = 0
        sign = 1
        stack = []
        for c in s:
            if c in "1234567890":
                num = num * 10 + int(c)
            elif c == "+":
                ans += sign * num
                num = 0
                sign = 1
            elif c == "-":
                ans += sign * num
                num = 0
                sign = -1
            elif c == "(":
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif c == ")":
                ans += sign * num
                num = 0
                ans *= stack.pop()
                ans += stack.pop()
        ans += sign * num
        return ans        
