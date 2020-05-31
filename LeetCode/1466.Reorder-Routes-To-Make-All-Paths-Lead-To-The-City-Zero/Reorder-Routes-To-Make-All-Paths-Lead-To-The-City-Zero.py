class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        g1 = collections.defaultdict(set)
        g2 = collections.defaultdict(set)
        for v, w in connections:
            g1[v].add(w)
            g1[w].add(v)
            g2[v].add(w)
            
        queue = collections.deque([0])
        res = 0
        seen = set([0])
        #print(g1)
        #print(g2)
        while queue:
            cur = queue.popleft()
            for n in g1[cur]:
                if n not in seen:
                    #print(cur, n)
                    if cur not in g2[n]: 
                        #print(cur, n, "@")
                        res += 1
                    queue.append(n)
                    seen.add(n)
        return res
        
