class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        
        crt = []
        pcrt = []
        edges_i = [(i, u, v, w) for i, (u, v, w) in enumerate(edges)]
        edges_i.sort(key = lambda x: x[3])
        mst = self.find_mst(n, edges_i, -1, -1)

        for i, (u, v, w) in enumerate(edges):
            if self.find_mst(n, edges_i, -1, i) > mst: crt.append(i)
            elif self.find_mst(n, edges_i, i, -1) == mst: pcrt.append(i)
      
        return [crt] + [pcrt]
                
        
    def find_mst(self, n, edges_i, use, not_use):
        self.father = {i: i for i in range(n)}
        self.n_edges = 0
        
        def find(a):
            x = a
            while x != self.father[x]:
                x = self.father[x]
                
            while x != self.father[a]:
                a, self.father[a] = self.father[a], x
                
            return x
        
        def union(a, b):
            A, B = find(a), find(b)
            if A != B:
                self.n_edges += 1
                self.father[A] = B
                
        res = 0
        mincost = deque([])
            
        for i, u, v, w in edges_i:
            if i != use and i != not_use:
                mincost.append((w, u, v))
            if use == i:
                res += w
                union(u, v)
                
        while mincost and self.n_edges != n - 1:
            cost, u, v = mincost.popleft()
            p_n_edges = self.n_edges
            union(u, v)
            if p_n_edges != self.n_edges:
                res += cost
       
        return res if self.n_edges == n - 1 else float('inf')
