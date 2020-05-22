class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        return self.canFinish1(numCourses, prerequisites)
    # DFS
    def canFinish2(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        visit = [0] * numCourses
        for c0, c1 in prerequisites:
            graph[c1].append(c0)
            
        for i in range(numCourses):
            if not self.dfs(i, graph, visit): return False
            
        return True
        
    def dfs(self, cur, graph, visit):
        if visit[cur] == -1: return False
        if visit[cur] == 1: return True
        
        visit[cur] = -1
        for n in graph[cur]:
            if not self.dfs(n, graph, visit): return False
            
        visit[cur] = 1
        return True
        
    # topological sort, Time: O(V+E), Space: O(V+E)
    def canFinish1(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        in_deg = [0] * (numCourses)
        cnt = 0
        for c0, c1 in prerequisites:
            graph[c1].append(c0)
            in_deg[c0] += 1
            
        queue = collections.deque()
        for i in range(numCourses):
            if in_deg[i] == 0: 
                queue.append(i)
                
        while queue:
            c = queue.popleft()
            cnt += 1
            for n in graph[c]:
                in_deg[n] -= 1
                if in_deg[n] == 0:
                    queue.append(n)
        
        return cnt == numCourses
        
        
