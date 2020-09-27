class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        res = 0
        for mask in range(2 << len(requests) - 1):
            deg = [0] * n
            cur = 0
            for i, (x, y) in enumerate(requests):
                if (mask >> i) & 1: continue
                cur += 1
                deg[x] -= 1
                deg[y] += 1
            if deg == [0] * n:
                res = max(res, cur)
        return res
                
            
        
        
        
        
        
