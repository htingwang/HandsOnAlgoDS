class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if c == ")":
                cur = ""
                while stack[-1] != "(":
                    cur += stack.pop()
                stack.pop()
                for tmp in cur:
                    stack.append(tmp)
            else:
                stack.append(c)
        return "".join(stack)
        
