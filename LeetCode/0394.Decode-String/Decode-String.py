class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        stack = []
        left = 0
        for i in range(len(s)):
            if s[i] == "]":
                cur, num = "", ""
                while stack[-1] != "[":
                    cur = stack.pop() + cur
                stack.pop()
                left -= 1
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                cur = cur * int(num)
                if len(stack): stack.append(cur)
                else: ans = ans + cur
            else:
                if s[i] == "[": left += 1
                stack.append(s[i])
            cur = ""
            #print("]".isalpha())
            while stack and stack[-1].isalpha() and (i == len(s) - 1 or s[i + 1].isdigit()) and left == 0:
                cur = stack.pop() + cur
            ans = ans + cur
        return ans
        
