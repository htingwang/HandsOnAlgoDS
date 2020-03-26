class Solution:
    def calculate(self, s: str) -> int:
        ans = num = cur = 0
        sign = "+"
        stack = []
        for c in s:
            if c in "1234567890":
                num = num * 10 + int(c)
            elif c in "+-*/":
                cur = self.update(sign, num, cur)
                sign, num = c, 0
                if c in "+-":
                    ans += cur
                    cur = 0
        cur = self.update(sign, num, cur)
        ans += cur
        return ans
    
    def update(self, sign, num, cur):
        if sign == "+":
            cur += num
        if sign == "-":
            cur -= num
        if sign == "*":
            cur *= num
        if sign == "/":
            if cur // num < 0 and cur % num != 0:
                cur = cur // num + 1
            else:
                cur //= num
        return cur
            
