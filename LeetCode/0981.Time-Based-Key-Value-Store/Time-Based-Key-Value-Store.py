class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maps = collections.defaultdict(list)
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.maps[key].append((value, timestamp))
        #print(self.maps)
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key in self.maps:
            left, right = 0, len(self.maps[key]) - 1
            while left < right:
                mid = (left + right) // 2
                if self.maps[key][mid][1] <= timestamp:
                    left = mid + 1
                else:
                    right = mid
            if self.maps[key][left][1] <= timestamp:
                return self.maps[key][left][0]
            elif left >= 1: return self.maps[key][left - 1][0]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
