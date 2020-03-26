import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, -stone)
        
        while len(maxheap) > 1:
            w1 = -heapq.heappop(maxheap)
            w2 = -heapq.heappop(maxheap)
            if w1 != w2:
                heapq.heappush(maxheap, -abs(w1 - w2))
        if maxheap: return -maxheap[0]
        return 0
