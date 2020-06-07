class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        res = list(costs[0])
        n = len(costs)
        for i in range(1, n):
            cur = list(costs[i])
            cur[0] += min(res[1], res[2])
            cur[1] += min(res[0], res[2])
            cur[2] += min(res[0], res[1])
            res = list(cur)
        return min(res)
