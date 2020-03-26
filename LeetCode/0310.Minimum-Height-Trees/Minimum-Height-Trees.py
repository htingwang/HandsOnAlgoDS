class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        adj = collections.defaultdict(list)
        ans = []
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        queue = collections.deque()
        
        for node in adj:
            if len(adj[node]) == 1:
                queue.append(node)
        
        while n > 2:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                #print node, adj
                adj[adj[node][0]].remove(node)
                #print adj
                if len(adj[adj[node][0]]) == 1:
                       queue.append(adj[node][0])
            n -= size
            
        for node in queue:
            ans.append(node)
        return ans
