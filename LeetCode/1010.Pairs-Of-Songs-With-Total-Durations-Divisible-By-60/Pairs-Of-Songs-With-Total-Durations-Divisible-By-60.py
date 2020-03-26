class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        ans = 0;
        exists = {};
        for x in time:
            if (exists.get(-x%60)): ans += (exists.get(-x%60));
            exists[x%60] = exists.get(x%60, 0)+1;
        return ans;
        
        
