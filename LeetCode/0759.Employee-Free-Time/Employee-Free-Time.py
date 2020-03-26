"""
# Definition for an Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import collections
class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: list<list<Interval>>
        :rtype: list<Interval>
        """
        count = collections.defaultdict(int)
        for employee in schedule:
            for interval in employee:
                count[interval.start] += 1
                count[interval.end] -= 1
        res = []
        start = end = 0
        cur = 0
        for time, num in sorted(count.items()):
            cur += num
            if cur == 0:
                start = time
            elif start != end:
                end = time
                if start < end:
                    res.append(Interval(start, end))
                start = end
        return res

        
