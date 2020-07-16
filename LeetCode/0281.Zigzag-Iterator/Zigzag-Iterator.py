class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.queue = collections.deque()
        if v1: self.queue.append(collections.deque(v1))
        if v2: self.queue.append(collections.deque(v2))
        

    def next(self):
        """
        :rtype: int
        """
        v = self.queue.popleft()
        res = v.popleft()
        if v: self.queue.append(v)
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) != 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
