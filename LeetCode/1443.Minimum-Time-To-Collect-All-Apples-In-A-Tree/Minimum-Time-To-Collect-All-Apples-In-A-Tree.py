class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        return self.dfs(0, seen, hasApple, graph)
        
    def dfs(self, u, seen, hasApple, graph):
        seen.add(u)
        res = 0
        for v in graph[u]:
            if v not in seen:
                res += self.dfs(v, seen, hasApple, graph)
        if u != 0 and (res or hasApple[u]): res += 2
        #print(u, res)
        return res
