class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        graph = {}
        in_degree = {}
        queue = collections.deque()
        ans = ""
        
        for i in range(len(words)):
            for j in range(len(words[i])):
                graph[words[i][j]] = set()
        
        for i in range(len(words) - 1):
            col = min(len(words[i]), len(words[i + 1]))
            for j in range(col):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
            if j == col and len(words[i]) > len(words[i + 1]):
                return ""
            
        for node in graph:
            if node not in in_degree: in_degree[node] = 0
            for neighbor in graph[node]:
                in_degree[neighbor] = in_degree.get(neighbor, 0) + 1
        #print in_degree       
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)
                ans += node
                
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                #print node, neighbor, ans
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    ans += neighbor
        
        if len(ans) == len(graph): return ans 
    
        return ""    
