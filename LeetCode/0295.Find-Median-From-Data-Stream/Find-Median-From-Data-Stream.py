class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.minheap, num)
        heapq.heappush(self.maxheap, -self.minheap[0])
        heapq.heappop(self.minheap)
        
        if len(self.minheap) < len(self.maxheap):
            heapq.heappush(self.minheap, -self.maxheap[0])
            heapq.heappop(self.maxheap)
        

    def findMedian(self):
        """
        :rtype: float
        """
        #print self.minheap, self.maxheap
        #print len(self.minheap) , len(self.maxheap)
        #if len(self.maxheap) == 0: return 0
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2.0
        return self.minheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
