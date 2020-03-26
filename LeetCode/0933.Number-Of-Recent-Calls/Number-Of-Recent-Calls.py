class RecentCounter(object):

    def __init__(self):
        self.timelist = [];

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.timelist.append(t);
        
        lo,hi = 0, len(self.timelist) - 1;
        while (lo < hi):
            mid = (lo + hi)/2;
            if (t-self.timelist[mid] <= 3000) and (t-self.timelist[mid+1] <= 3000):
                hi = mid;
            else:
                lo = mid+1;

        self.timelist = self.timelist[lo:];
        #print(self.timelist)
        return len(self.timelist);
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
