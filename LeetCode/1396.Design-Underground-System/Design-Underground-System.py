class UndergroundSystem(object):

    def __init__(self):
        self.checkin = {}
        self.diff = collections.defaultdict(int)
        self.count = collections.defaultdict(int)
        

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkin[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        sin, tin = self.checkin[id]
        self.diff[sin + "," + stationName] += t - tin
        self.count[sin + "," + stationName] += 1
        

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return float(self.diff[startStation + "," + endStation]) / self.count[startStation + "," + endStation]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
