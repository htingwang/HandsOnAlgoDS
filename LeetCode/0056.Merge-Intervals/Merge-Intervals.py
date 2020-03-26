class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals.sort()
        for i, interval in enumerate(intervals):
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else: # cur start <= prev end
                res[-1][1] = max(res[-1][1], interval[1])
        return res
