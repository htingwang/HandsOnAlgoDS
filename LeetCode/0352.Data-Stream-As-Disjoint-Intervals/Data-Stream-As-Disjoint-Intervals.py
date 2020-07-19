class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: None
        """
        left = right = val
        i = bisect.bisect(self.intervals, [left, right])
        l_intervals, r_intervals = self.intervals[: i], self.intervals[i :]
        
        if i < len(self.intervals) and right >= self.intervals[i][0] - 1: 
            right = self.intervals[i][1]
            left = min(left, self.intervals[i][0])
            r_intervals = r_intervals[1 : ]
        if i > 0 and left <= self.intervals[i - 1][1] + 1: 
            left = self.intervals[i - 1][0]
            right = max(right, self.intervals[i - 1][1])
            l_intervals = l_intervals[: -1]
                
        self.intervals = l_intervals + [[left, right]] + r_intervals
        
    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
