class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        return self.findOrder1(numCourses, prerequisites)
    
    # DFS, Time: O(V+E), Space: O(V+E)
    def findOrder2(self, numCourses, prerequisites):
        res = []
        graph = collections.defaultdict(list)
        visit = [0] * numCourses
        for c0, c1 in prerequisites:
            graph[c1].append(c0)
        for i in range(numCourses):
            if not self.dfs(i, graph, visit, res): return []     
        return res[:: -1]
    
    def dfs(self, cur, graph, visit, res):
        if visit[cur] == -1: return False
        if visit[cur] == 1: return True

        visit[cur] = -1
        for n in graph[cur]:
            if not self.dfs(n, graph, visit, res): return False  
        visit[cur] = 1
        
        res.append(cur)
        return True
    
    # topological sort, Time: O(V+E), Space: O(V+E)
    def findOrder1(self, numCourses, prerequisites):
        res = []
        graph = collections.defaultdict(list)
        in_deg = [0] * numCourses
        
        for c0, c1 in prerequisites:
            graph[c1].append(c0)
            in_deg[c0] += 1
            
        queue = collections.deque()
        for i in range(numCourses):
            if in_deg[i] == 0:
                queue.append(i)
                
        while queue:
            c = queue.popleft()
            res.append(c)
            for n in graph[c]:
                in_deg[n] -= 1
                if in_deg[n] == 0:
                    queue.append(n)
                    
        return res if len(res) == numCourses else []
