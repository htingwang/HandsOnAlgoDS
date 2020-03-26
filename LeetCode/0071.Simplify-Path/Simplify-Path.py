class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        
        i = 0
        while i < len(path):
            while i < len(path) and path[i] == "/":
                i += 1
                
            j = i
            while j < len(path) and path[j] != "/":
                j += 1
                
            if path[i : j] == "..":
                if stack: stack.pop()
            elif path[i : j] != "." and i != j:
                stack.append(path[i : j])
            i = j
        print(stack)
        res = ""
        for name in stack:
            res += "/" + name
        return res if stack else "/"
