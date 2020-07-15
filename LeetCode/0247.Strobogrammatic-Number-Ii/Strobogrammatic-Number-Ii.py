class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def dfs(m):
            if m == 0: return [""]
            if m == 1: return ["0", "1", "8"]
            res = []
            t = dfs(m - 2)
            for a in t:
                if n != m: res.append("0" + a + "0")
                res.append("1" + a + "1")
                res.append("6" + a + "9")
                res.append("8" + a + "8")
                res.append("9" + a + "6")
            return res
        
        return dfs(n)
        
