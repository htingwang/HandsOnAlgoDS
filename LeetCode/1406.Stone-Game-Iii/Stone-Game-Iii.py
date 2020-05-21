class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        return self.stoneGameIII2(stoneValue)
    
    # Space:O(1)
    def stoneGameIII2(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * 3
        for i in range(n - 1, -1, -1):
            take = 0
            cur = float('-inf')
            for j in range(3):
                if i + j < n: 
                    take += stoneValue[i + j]
                    cur = max(cur, take - dp[(i + j + 1) % 3])
            dp[i % 3] = cur
            #print(dp)
        if dp[0] > 0: return "Alice"
        if dp[0] < 0: return "Bob"
        return "Tie"
        
    # Space:O(n)
    def stoneGameIII1(self, stoneValue):
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            take = 0
            for j in range(3):
                if i + j < n: 
                    take += stoneValue[i + j]
                    dp[i] = max(dp[i], take - dp[i + j + 1])
        if dp[0] > 0: return "Alice"
        if dp[0] < 0: return "Bob"
        return "Tie"
