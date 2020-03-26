class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        start, end = newInterval
        idx, n = 0, len(intervals)
        
        while idx < n:
            if intervals[idx][0] < start:
                res.append(intervals[idx])
                idx += 1
            else: break
        #print(res)
        if not res or res[-1][1] < start:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], newInterval[1])

        while idx < n:
            if not res or res[-1][1] < intervals[idx][0]:
                res.append(intervals[idx])
            else:
                res[-1][1] = max(res[-1][1], intervals[idx][1])
            idx += 1
        
        return res
