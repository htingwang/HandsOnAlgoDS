class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        res = 1
        count = collections.defaultdict(int)
        if len(croakOfFrogs) % 5 != 0: return -1
        max_frog = len(croakOfFrogs) / 5
        intervals = [0] * len(croakOfFrogs)
        for i, ch in enumerate(croakOfFrogs):
            if ch == "c": 
                intervals[i] = 1
                count["c"] += 1   
            if ch == "r":
                count["r"] += 1
                if count["r"] > count["c"]: return -1
            if ch == "o":
                count["o"] += 1
                if count["o"] > count["r"]: return -1
            if ch == "a":
                count["a"] += 1
                if count["a"] > count["o"]: return -1
            if ch == "k":
                intervals[i] = -1
                count["k"] += 1
                if count["k"] > count["a"]: return -1
        if count["c"] == count["r"] == count["o"] == count["a"] == count["k"]:
            res = 1
            cur = 0
            for n in intervals:
                cur += n
                res = max(res, cur)
            return res
        return -1
