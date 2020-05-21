class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        n = len(startTime)
        res = 0
        for i in range(n):
            if startTime[i] <= queryTime <= endTime[i]: res += 1
        return res
