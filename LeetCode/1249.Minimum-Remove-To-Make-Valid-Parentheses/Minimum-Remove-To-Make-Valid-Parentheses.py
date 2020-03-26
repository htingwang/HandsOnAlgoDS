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
            elif c == ")":
                if stack_left:
                    stack_left.pop()
                else:
                    stack_right.append(i)
        remove_idx = set(stack_left + stack_right)
        res = ""
        #print(remove_idx)
        for i, c in enumerate(s):
            if i not in remove_idx:
                #print(i, i not in remove_idx)
                res += c
        return res
        
