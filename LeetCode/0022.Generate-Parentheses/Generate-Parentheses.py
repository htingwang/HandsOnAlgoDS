class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(n, left, right, sol, ans):
            #print sol, ans
            if left == right == n:
                #print sol
                ans.append(sol)
            if left > n: return
            if left > right:
                #sol += ")"
                dfs(n, left, right + 1, sol + ")", ans)
                #sol = sol[:-1]
            #sol += "("
            dfs(n, left + 1, right, sol + "(", ans)
            #sol = sol[:-1]
                
                
        ans = []
        left = right = 0
        dfs(n, left, right, "", ans)
        return ans
        
