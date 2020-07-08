class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c in set(["+", "-", "*", "/"]):
                b, a = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(a + b)
                if c == "-":
                    stack.append(a - b)
                if c == "*":
                    stack.append(a * b)
                if c == "/":
                    if (a > 0 and b < 0) or (a < 0 and b > 0):
                        stack.append(abs(a) // abs(b) * -1)
                    else:
                        stack.append(abs(a) // abs(b))
            else:
                stack.append(int(c))
        return stack[0]
