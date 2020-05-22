class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        return self.minimumSemesters2(N, relations)
    
    # DFS, Time: O(V+E), Space: O(V+E)
    def minimumSemesters2(self, N, relations):
        res = float('-inf')
        graph = collections.defaultdict(list)
        memo = [0] * (1 + N)
        for c0, c1 in relations:
            graph[c0].append(c1)
        for i in range(1, N + 1):
            sem = self.dfs(i, graph, memo)
            if sem == -1: return -1
            res = max(res, sem)
        return res
    
    def dfs(self, cur, graph, memo):
        if memo[cur] == -1: return -1
        if memo[cur] != 0: return memo[cur]
        
        res = 1
        memo[cur] = -1
        for n in graph[cur]:
            sem = self.dfs(n, graph, memo)
            if sem == -1: return -1
            res = max(res, sem + 1)
        memo[cur] = res
        return res
            
        
    # topological sort, Time: O(V+E), Space: O(V+E)
    def minimumSemesters1(self, N, relations):
        res = 0
        graph = collections.defaultdict(list)
        in_deg = [0] * (N + 1)
        cnt = 0
        for c0, c1 in relations:
            graph[c0].append(c1)
            in_deg[c1] += 1
            
        queue = collections.deque()
        for i in range(1, N + 1):
            if in_deg[i] == 0:
                queue.append(i)

        while queue:
            s = len(queue)
            for _ in range(s):
                c = queue.popleft()
                cnt += 1
                for n in graph[c]:
                    in_deg[n] -= 1
                    if in_deg[n] == 0:
                        queue.append(n)
            res += 1
            
        return res if cnt == N else -1
            
                
                
        
        
