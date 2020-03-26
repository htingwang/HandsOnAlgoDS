class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        cur = [0] * 1000
        for trip in trips:
            cur[trip[1]] += trip[0]
            cur[trip[2]] -= trip[0]
        need = 0
        for i in range(len(cur)):
            need += cur[i]
            if need > capacity:
                return False
        return True
        
