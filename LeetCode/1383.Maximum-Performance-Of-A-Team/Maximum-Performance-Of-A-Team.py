class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        minheap = []
        s_sum = 0
        for e, s in sorted(zip(efficiency, speed), reverse = 1):
            s_sum += s
            heapq.heappush(minheap, s)
            if len(minheap) > k:
                s_sum -= heapq.heappop(minheap)
            res = max(res, s_sum * e)
        return res % (10 ** 9 + 7)
