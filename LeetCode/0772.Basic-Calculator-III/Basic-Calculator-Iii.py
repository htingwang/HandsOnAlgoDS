class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        op_stack = []
        i = num = 0
        
        #return 0
        #for c in s:
        while i < len(s):
            c = s[i]
            if c in "1234567890":
                num = num * 10 + int(c)
                if i == len(s) - 1 or s[i + 1] not in "1234567890":
                    #print(num)
                    num_stack.append(num)
                    #if len(op_stack) > 1: print(op_stack[-2])
                    #if op_stack and op_stack[-1] == "-":
                    #    if len(op_stack) == 1 or op_stack[-2] == "(":
                    #        num_stack[-1] = num_stack[-1] * (-1)
                    #    op_stack.pop()
                    num = 0
            if c == "(":
                op_stack.append(c)
            if c == ")":
                #print(i, op_stack)
                while op_stack[-1] != "(":
                    num_stack.append(self.operation(op_stack.pop(), num_stack.pop(), num_stack.pop()))
                op_stack.pop()
            if c in "+-*/":
                if c == "-":
                    if i == 0 or s[i - 1] == "(":
                        num_stack.append(0)
                while op_stack and self.precedence(c, op_stack[-1]):
                    num_stack.append(self.operation(op_stack.pop(), num_stack.pop(), num_stack.pop()))
                op_stack.append(c)
            i += 1
            #print(op_stack, num_stack)
        #print(op_stack, num_stack)
        while op_stack:
            #print(op_stack, num_stack)
            num_stack.append(self.operation(op_stack.pop(), num_stack.pop(), num_stack.pop()))
        return num_stack[-1]
        #return self.parse_expression(s, 0)[0]
    def precedence(self, op1, op2):    
        if op2 == "(" or op2 == ")": return False
        if (op1 == "*" or op1 == "/") and (op2 == "+" or op2 == "-"): return False
        return True
        
        

    def operation(self, op, b, a):
        #print(op, b, a)
        if op == "+": ans = a + b
        if op == "-": ans = a - b
        if op == "*": ans = a * b
        if op == "/": 
            if a // b < 0 and a % b != 0:
                ans = a // b + 1
            else:
                ans = a // b     
        return ans
    
    def parse_expression(self, s, start):
        ans = cur = num = 0
        i = start
        op = "+"
        while i < len(s) and s[i]  != ")":
            if i < len(s) and s[i] in "1234567890":
                num = num * 10 + int(s[i])
            elif i < len(s) and s[i] == "(":
                num, i = self.parse_expression(s, i + 1)    
            elif s[i] in "+-*/":
                cur = self.operation(op, cur, num)
                op, num = s[i], 0
                if s[i] in "+-":
                    ans += cur
                    cur = 0
            i += 1
        cur = self.operation(op, cur, num)
        ans += cur
        return (ans, i)
    
    def operation2(self, op, cur, num):
        ans = 0
        if op == "+": ans = cur + num
        if op == "-": ans = cur - num
        if op == "*": ans = cur * num
        if op == "/": 
            if cur // num < 0 and cur % num != 0:
                ans = cur // num + 1
            else:
                ans = cur // num     
        return ans
