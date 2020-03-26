class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = [[0, 0]] * 300
        #print("aaa")

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        #print("bbb")
        i = timestamp % 300
        time, hits = self.q[i]
        if time != timestamp:
            self.q[i] = timestamp, 1
        else:
            self.q[i] = time, hits + 1
    
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        #print("ccc")
        res = 0
        for i in range(300):
            if timestamp - self.q[i][0] < 300:
                res += self.q[i][1]
        return res
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
