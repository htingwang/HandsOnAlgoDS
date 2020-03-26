class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        minheap = []
        res = 0
        for stick in sticks:
            heapq.heappush(minheap, stick)
            
        while len(minheap) > 1:
            x, y = heapq.heappop(minheap), heapq.heappop(minheap)
            res += (x + y)
            heapq.heappush(minheap, x + y)
            
        return res
            
        
