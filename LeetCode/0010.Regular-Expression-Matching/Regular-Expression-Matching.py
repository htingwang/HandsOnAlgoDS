class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #### Dynamic Programmint ####
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            #1print j
            if p[j - 1] == "*": dp[0][j] = dp[0][j - 2]
                
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2] or ((s[i - 1] == p[j - 2] or p[j - 2] == ".") and dp[i - 1][j])
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == ".") and dp[i - 1][j - 1]
                    
        return dp[len(s)][len(p)]
        
        
        #### Recursion #####
        def dfs(s, i, p, j, memo):
            #print i, j, memo
            if (i, j) in memo: return memo[(i, j)]
            
            if len(s) == i:
                #print len(p), j
                if (len(p) - j) % 2 == 1: return False
                for k in range((len(p) - j) / 2):
                    #print j, k, j+k*2
                    if p[j + k * 2 + 1] != "*": return False
                return True
            
            if len(p) == j: return False
            
            if j + 1 < len(p) and p[j + 1] == "*":
                memo[(i, j)] = ((s[i] == p[j] or p[j] == ".") and dfs(s, i + 1, p, j, memo)) or dfs(s, i, p, j + 2, memo)
            else:
                memo[(i, j)] = (s[i] == p[j] or p[j] == ".") and dfs(s, i + 1, p, j + 1, memo)
            
            return memo[(i, j)]
                                
        return dfs(s, 0, p, 0, {})
        
