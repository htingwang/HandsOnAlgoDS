class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        graph = collections.defaultdict(list)
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            indegree[c1] += 1
            
        queue = collections.deque()
        for i, deg in enumerate(indegree):
            if deg == 0:
                queue.append(i)
                
        while queue:
            cur = queue.popleft()
            if cur in graph:
                for n_course in graph[cur]:
                    indegree[n_course] -= 1
                    if indegree[n_course] == 0:
                        queue.append(n_course)
                    
        for deg in indegree:
            if deg != 0:
                return False
            
        return True
            
