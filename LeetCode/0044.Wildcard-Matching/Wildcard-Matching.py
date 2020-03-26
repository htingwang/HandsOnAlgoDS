class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def dfs(s, i, p, j, memo):
            #print i, j, memo
            if (i, j) in memo: return memo[(i, j)]
            
            if len(s) == i:
                for k in range(j, len(p)):
                    if p[k] != "*": return False
                return True
            
            if len(p) == j: return False
            
            if p[j] == "*":
                memo[(i, j)] = dfs(s, i + 1, p, j, memo) or dfs(s, i, p, j + 1, memo)
            else:
                memo[(i, j)] = (s[i] == p[j] or p[j] == "?") and dfs(s, i + 1, p, j + 1, memo)
            
            return memo[(i, j)]
            
        #return dfs(s, 0, p, 0, {})       

        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]   
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*": dp[0][j] = dp[0][j - 1]
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                else:
                    dp[i][j] = (s[i - 1] == p[j - 1] or p[j - 1] == "?") and dp[i - 1][j - 1]
        return dp[len(s)][len(p)]
        
    

        
