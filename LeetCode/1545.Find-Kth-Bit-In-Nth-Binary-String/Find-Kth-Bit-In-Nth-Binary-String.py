class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k == 1: return "0"
        def dfs(n):
            if n == 1:
                return "0"
            pre = dfs(n - 1)
            digit = pow(2, n - 1) - 1
            pre += "1"
            for i in range(digit - 1, -1, -1):
                if pre[i] == "0":
                    pre += "1"
                else:
                    pre += "0"
            #print(n, pre, digit)
            return pre
            
        s = dfs(n)
        #print(s)
        return s[k - 1]
