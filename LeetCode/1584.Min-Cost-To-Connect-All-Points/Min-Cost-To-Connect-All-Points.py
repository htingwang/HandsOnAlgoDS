class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dist(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        minheap = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(minheap, (dist(points[i], points[j]), i, j))
                
        res = 0
        seen = set()
        e = 0
        f = [i for i in range(n)]
        def union(i, j):
            fi, fj = find(i), find(j)
            if fi == fj:
                return 1
            f[fi] = fj
            return 0
        
        def find(i):
            x = i
            while x != f[x]:
                x = f[x]
            
            a = x
            return x
        #print(minheap)
        while minheap:
            d, i, j = heapq.heappop(minheap)
            if union(i, j): continue
            e += 1
            res += d
            #print(d, i, j, f)
            if e == n - 1: break
                
        return res
