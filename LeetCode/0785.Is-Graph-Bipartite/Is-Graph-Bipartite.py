class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        self.parent = {x : x for x in range(len(graph))}
        
        for i in range(len(graph)):
            if not graph[i]:
                continue
                
            x = self.find(i)
            y = self.find(graph[i][0])
            
            for j in range(1, len(graph[i])):
                root = self.find(graph[i][j])
                if root == x:
                    return False
                self.parent[root] = y
        return True
        
    def find(self, x):
        return x if x == self.parent[x] else self.find(self.parent[x])
