class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        ratio = []
        n = len(quality)
        for i in range(n):
            ratio.append(float(wage[i]) / quality[i])
        
        maxheap = []
        res = float('inf')
        q_sum = 0
        for r, q in sorted(zip(ratio, quality)):
            q_sum += q
            heapq.heappush(maxheap, -q)
            if len(maxheap) > K:
                q_sum += heapq.heappop(minheap)
            if len(maxheap) == K: res = min(res, q_sum * r)
        return res
