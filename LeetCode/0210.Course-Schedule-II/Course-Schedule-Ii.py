from collections import deque, defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for p in prerequisites:
            graph[p[1]].append(p[0])
            in_degree[p[0]] += 1
            
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)
            for i in graph[cur]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)
                    
        return res if len(res) == numCourses else []
