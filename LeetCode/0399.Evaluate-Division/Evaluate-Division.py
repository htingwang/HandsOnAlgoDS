class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = collections.defaultdict(set)
        for i, (x, y) in enumerate(equations):
            g[x].add((y, float(values[i])))
            g[y].add((x, 1.0 / values[i]))
            g[x].add((x, 1.0))
            g[y].add((y, 1.0))
        res = []
        for x, y in queries:
            if x not in g or y not in g: 
                res.append(-1)
                continue
            queue = collections.deque()
            seen = set()
            found = False
            queue.append((x, 1))
            seen.add(x)
            #print(g)
            while queue:
                size = len(queue)
                for i in range(size):
                    a, b = queue.popleft()
                    #print(a, b)
                    if a == y:
                        found = True
                        res.append(b)
                        break
                    for c, d in g[a]:
                        if c in seen: continue
                        seen.add(c)
                        queue.append((c, b * d))
            if not found: res.append(-1)
        return res

