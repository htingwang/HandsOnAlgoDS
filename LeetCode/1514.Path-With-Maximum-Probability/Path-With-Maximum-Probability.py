class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        """
        w = collections.defaultdict(list)
        for i, (u, v) in enumerate(edges):
            w[u].append((v, succProb[i]))
            w[v].append((u, succProb[i]))
        minheap = [(-1, start)]
        seen = set()
        res = 0
        while minheap:
            cost, u = heapq.heappop(minheap)
            seen.add(u)
            if u == end:
                res = max(res, -cost)
            for v, ncost in w[u]:
                if v not in seen:
                    heapq.heappush(minheap, (ncost * cost, v))
        return res
