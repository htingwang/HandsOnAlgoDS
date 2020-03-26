class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        first = second = [-1, -1]
        father = [-1] * (n + 1)
        
        for i, [u, v] in enumerate(edges):
            if father[v] == -1:
                father[v] = u
            else:
                first = [father[v], v]
                second = [u, v]
                edges[i][1] = 0
        
        father = [-1] * (n + 1)
        for u, v in edges:
            if v == 0: continue
            x = self.find(father, u)
            y = self.find(father, v)
            if x == y: 
                if first[0] == -1: return [u, v]
                return first
            father[v] = u 
        return second
            
    def find(self, father, node):
        while father[node] != -1:
            node = father[node]
        return node
        
