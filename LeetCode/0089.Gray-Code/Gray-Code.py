class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return self.grayCode3(n)
    
    def grayCode1(self, n):
        res = []
        for i in range(pow(2, n)):
            res.append(i ^ (i >> 1))
        return res
    
    def grayCode2(self, n):
        res = [0]
        for i in range(n):
            size = len(res)
            for j in range(size - 1, -1, -1):
                res.append(res[j] | (1 << i))
        return res
    
    def grayCode3(self, n):
        res = []
        seen = set()
        def dfs(n, cur):
            res.append(cur)
            seen.add(cur)
            if len(res) == pow(2, n): return
            for i in range(n):
                if cur ^ (1 << i) not in seen:
                    dfs(n, cur ^ (1 << i))
                    
        dfs(n, 0)
        return res
            
        
