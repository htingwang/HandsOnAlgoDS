class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        graph = collections.defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)
        self.time = 0
        low = {}
        disc = {}
        parent = [-1] * n
        visited = set()
        #print(graph)
        self.dfs(0, graph, parent, disc, low, visited, res)
        return res
    
    def dfs(self, u, graph, parent, disc, low, visited, res):
        visited.add(u)
        low[u] = disc[u] = self.time
        self.time += 1
        
        for v in graph[u]:
            if v not in visited:
                parent[v] = u
                self.dfs(v, graph, parent, disc, low, visited, res)
                low[u] = min(low[u], low[v])
                #print(u, v, disc[u], disc[v], low[u], low[v])
                if low[v] > disc[u]:
                    res.append([u, v])
            elif parent[u] != v:
                low[u] = min(low[u], disc[v])
                #print(u,v, low[u])
