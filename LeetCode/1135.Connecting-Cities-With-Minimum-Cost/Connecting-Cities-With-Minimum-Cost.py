class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int
        """
        res = 0
        self.father = {}
        self.edges = 0
        for i in range(1, N + 1): self.father[i] = i
        mincost = []
        for u, v, cost in connections: heapq.heappush(mincost, (cost, u, v))
        while mincost and self.edges != N - 1:
            cost, u, v = heapq.heappop(mincost)
            edges = self.edges
            self.union(u, v)
            if edges != self.edges:
                res += cost
        return res if self.edges == N - 1 else -1
            
    def union(self, a, b):
        A, B = self.find(a), self.find(b)
        if A != B:
            self.father[A] = B
            self.edges += 1
    
    def find(self, a):
        x = a
        while x != self.father[x]:
            x = self.father[x]
            
        while x != self.father[a]:
            a, self.father[a] = self.father[a], x
            
        return x
        
