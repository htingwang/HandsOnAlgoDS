class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        rootA = range(n + 1)
        res = e1 = e2 = 0
        
        def find(i, root):
            x = i
            while x != root[x]:
                x = root[x]
            while x != root[i]:
                i, root[i] = root[i], x
            return x
        
        def union(x, y, root):
            X, Y = find(x, root), find(y, root)
            if X == Y: return 0
            root[X] = Y
            return 1
        
        for t, u, v in edges:
            if t == 3:
                if union(u, v, rootA):
                    e1 += 1
                else:
                    res += 1
                    
        e2 = e1
        rootB = list(rootA)
        
        for t, u, v in edges:
            if t == 1:
                if union(u, v, rootA):
                    e1 += 1
                else:
                    res += 1
            elif t == 2:
                if union(u, v, rootB):
                    e2 += 1
                else:
                    res += 1
        return res if e1 ==e2 == n - 1 else -1
