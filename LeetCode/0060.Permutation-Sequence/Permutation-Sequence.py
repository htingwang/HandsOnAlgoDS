class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        P = [1] * (n + 1)
        for i in range(1, n + 1): P[i] = P[i - 1] * i
        
        s = ""
        for i in range(1, n + 1): s += str(i)
            
        def dfs(s, i):
            l = len(s)
            if l == 1: return s
            idx, ni = i // P[l - 1], i % P[l - 1]
            return s[idx] + dfs(s[: idx] + s[idx + 1 :], ni) 
            
            
        return dfs(s, k - 1)
        
