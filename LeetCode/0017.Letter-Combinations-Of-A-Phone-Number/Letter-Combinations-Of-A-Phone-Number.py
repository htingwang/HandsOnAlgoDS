class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = [[], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        
        def dfs(digits, ans, cur):
            if len(digits) == 0: 
                ans.append(cur)
                return
            for char in mapping[int(digits[0])]:
                #cur += char
                dfs(digits[1:], ans, cur + char)
                #cur = cur[:-1]
            
        
        ans = []
        if len(digits) == 0: return ans
        #dfs(digits, ans, "")
        
        #### simulation without recursion ####
        for i in range(len(digits)):
            tmp = []
            for j in range(len(mapping[int(digits[i])])):
                if len(ans) > 0:
                    for k in range(len(ans)):
                        tmp.append(ans[k] + mapping[int(digits[i])][j])
                else:
                    tmp.append(mapping[int(digits[i])][j])
        
            ans = tmp[:]
        #### simulation without recursion ####
        return ans
        
