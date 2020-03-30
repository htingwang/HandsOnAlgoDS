class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack_left = []
        stack_right = []
        for i, c in enumerate(s):
            if c == "(":
                stack_left.append(i)
            if c == ")":
                if stack_left:
                    stack_left.pop()
                else:
                    stack_right.append(i)
        res = []
        #res = ""
        rm_set = set(stack_left + stack_right)
        for i, c in enumerate(s):
            if i not in rm_set:
                res.append(c)
                #res += c # This is slower
        return "".join(res)
        
