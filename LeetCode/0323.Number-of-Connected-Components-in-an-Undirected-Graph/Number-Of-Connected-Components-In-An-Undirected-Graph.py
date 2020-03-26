class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = set()
        res = 0
        #print(graph)
        for i in range(n):
            if i in seen: continue
            res += 1
            stack = [i]
            while stack:
                cur = stack.pop()
                #print(i, cur, stack, seen)
                seen.add(cur)
                for j in graph[cur]:
                    if j not in seen: stack.append(j)
        return res
