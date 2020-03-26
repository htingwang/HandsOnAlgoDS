class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def cnt1(x):
            if x == "0": return 0
            if x == "*": return 9
            return 1
        
        def cnt2(x, y):
            if x == "0" or x > "2":
                return 0
            if x == "1":
                if y == "*": 
                    return 9
                return 1
            if x == "2":
                if y > "6": return 0
                if y == "*": return 6
                return 1
            # x == *
            if "0" <= y <= "6":
                return 2
            if "7" <= y <= "9":
                return 1
            
            # **
            return 15
        
        MOD = pow(10, 9) + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] * cnt1(s[i - 1])
            dp[i] = dp[i] % MOD
            #print(i, dp[i])
            if i > 1:
                dp[i] += dp[i - 2] * cnt2(s[i - 2], s[i - 1])
            dp[i] = dp[i] % MOD
        #print(dp)
        return dp[-1]
