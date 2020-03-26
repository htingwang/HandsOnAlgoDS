class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] * (len(days) + 1)
        dp[1] = min(costs)
        anchor = 1
        for i in range(2, len(dp)):
            #print i
            dp[i] = dp[1] + dp[i - 1]
            j = anchor
            check = 0
            while j < i:
                if days[i - 1] - days[j - 1] < 7 and check <= 1:
                    dp[i] = min(dp[i], dp[j - 1] + costs[1])
                    check += 1
                elif days[i - 1] - days[j - 1] < 30 and check == 0:
                    dp[i] = min(dp[i], dp[j - 1] + costs[2])
                    check += 1
                    anchor = j
                j += 1
        #print(dp)
        return dp[len(days)]
