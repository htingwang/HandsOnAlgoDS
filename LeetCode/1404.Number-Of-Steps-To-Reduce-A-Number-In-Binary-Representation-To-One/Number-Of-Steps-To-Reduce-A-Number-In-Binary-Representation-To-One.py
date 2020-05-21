class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in range(len(s)):
            num =num * 2 + int(s[i])
            #print(num)
        #print(num)
        return self.dfs(num)
    def dfs(self, n):
        if n == 1: return 0
        if n % 2 == 0: return 1 + self.dfs(n / 2)
        else: return 1 + self.dfs(n + 1)
