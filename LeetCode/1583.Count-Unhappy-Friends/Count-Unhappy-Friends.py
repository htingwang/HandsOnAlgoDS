class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        pre = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n - 1):
                pre[i][preferences[i][j]] = j
                
        pa = {}
        for i, j in pairs:
            pa[i] = j
            pa[j] = i
        
        # x prefers u over y, and
        # u prefers x over v.
        res = set()
        for x in range(n):
            for u in range(n):
                if x != u:
                    y, v = pa[x], pa[u]
                    if pre[x][u] < pre[x][y] and pre[u][x] < pre[u][v]:
                        res.add(x)
                        res.add(u)
                    
        return len(res)
