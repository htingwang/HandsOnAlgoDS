class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(set)
        for u, v, w in times:
            graph[u].add((v, w))
        dists = {}
        minheap = [(0, K)]
        while minheap:
            dist, node = heapq.heappop(minheap)
            if node in dists: continue
            dists[node] = dist
            for v, w in graph[node]:
                if v not in dists:
                    heapq.heappush(minheap, (dist + w, v))
        return max(dists.values()) if len(dists) == N else -1
