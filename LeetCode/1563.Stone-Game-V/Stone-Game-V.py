class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        pre = [0] * (n + 1)
        memo = [[-1] * n for _ in range(n)]
        for i in range(n):
            pre[i + 1] = pre[i] + stoneValue[i]
            
        def dfs(s, e):
            if memo[s][e] != -1: return memo[s][e]
            if s == e:
                memo[s][s] = 0
                return 0
            res = 0
            for i in range(s, e):
                left, right = pre[i + 1] - pre[s], pre[e + 1] - pre[i + 1]
                #print(i, left, right)
                if left > right:
                    res = max(res, right + dfs(i + 1, e))
                elif left < right:
                    res = max(res, left + dfs(s, i))
                else:
                    res = max(res, right + dfs(i + 1, e), left + dfs(s, i))
            memo[s][e] = res
            #print(s, e, res)
            return res
        return dfs(0, n - 1)
