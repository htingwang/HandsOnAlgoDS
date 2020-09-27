class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        res = mx = 0
        for i, c in enumerate(s):
            if i != 0 and c != s[i - 1]: mx = 0
            res += min(mx, cost[i])
            mx = max(mx, cost[i])
        return res


