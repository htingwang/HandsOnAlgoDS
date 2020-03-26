class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if not n or s[0] == "0": return 0
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if s[i - 1] == s[i - 2] == "0": return 0
            if s[i - 1] != "0":
                dp[i] = dp[i - 1]
            #print(i, dp[i], int(s[i - 1]) + 10 * int(s[i - 2]))
            #if 10 <= int(s[i - 1]) + 10 * int(s[i - 2]) <= 26:
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6") :
                dp[i] += dp[i - 2]
        return dp[n]
