class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        stack = []
        res = [""]
        
        i = 0
        left = 0
        while i < len(S):
            cur_str_list = []
            cur_str = ""
            while i < len(S) and (S[i].isalpha() or S[i] == ","):
                if S[i] != ",":
                    if left:
                        cur_str_list.append(S[i])
                    else:
                        cur_str += S[i]
                i += 1
                
            if cur_str:
                stack.append([cur_str])
            if cur_str_list:
                stack.append(cur_str_list)
                
            if i < len(S) and S[i] == "{":
                left = 1
            if i < len(S) and S[i] == "}":
                left = 0
                
            i += 1
        #print(stack)        
        while len(stack) > 1:
            stack.append(self.merge(stack.pop(), stack.pop()))
        stack[0].sort()     
        return stack[0]
    
    def merge(self, list2, list1):
        res = []
        for s1 in list1:
            for s2 in list2:
                res.append(s1 + s2)
        return res
