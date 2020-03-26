class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        
        stack = []
        i = 0
        
        while i < len(expression):
            cur_str = ""
            while i < len(expression) and expression[i].isalpha():
                cur_str += expression[i]
                i += 1
            if cur_str:
                cur_str_list = [cur_str]
                if stack and type(stack[-1]) == list:
                    cur_str_list = self.merge(cur_str_list, stack.pop())
                stack.append(cur_str_list)
                continue
                
            if expression[i] == "}":
                cur_str_list = []
                while stack[-1] != "{":
                    cur_str_list = stack.pop() + cur_str_list
                    if stack[-1] == ",":
                        stack.pop()
                stack.pop()
                if stack and type(stack[-1]) == list:
                    cur_str_list = self.merge(cur_str_list, stack.pop())
                stack.append(cur_str_list)
            else:
                stack.append(expression[i])
            i += 1
                
        return sorted(list(set(stack[0])))
                
        
    def merge(self, list2, list1):
        return [s1 + s2 for s1 in list1 for s2 in list2]
