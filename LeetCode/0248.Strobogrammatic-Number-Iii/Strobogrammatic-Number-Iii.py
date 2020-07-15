class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        def dfs(m, n):
            if m == 0: return [""]
            if m == 1: return ["0", "1", "8"]
            t = dfs(m - 2, n)
            res = []
            for a in t:
                if m != n: res.append("0" + a + "0")
                res.append("1" + a + "1")
                res.append("6" + a + "9")
                res.append("8" + a + "8")
                res.append("9" + a + "6")
            return res
        
        nums = []
        for n in range(len(low), len(high) + 1):
            nums += dfs(n, n)

        res = 0
        for num in nums:
            if len(num) == len(low) and num < low: continue
            if len(num) == len(high) and num > high: continue
            res += 1
        return res
        

