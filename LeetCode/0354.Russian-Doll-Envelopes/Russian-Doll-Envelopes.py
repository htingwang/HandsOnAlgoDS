class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        dp = []
        for w, h in envelopes:
            i = bisect.bisect_left(dp, h)
            if i == len(dp): dp.append(h)
            else: dp[i] = h
        return len(dp)
