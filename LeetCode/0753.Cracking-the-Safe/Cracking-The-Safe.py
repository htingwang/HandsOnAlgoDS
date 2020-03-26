class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """      
        cur = ""
        code = set()

        def guesscode(n, k, cur, code, res):
            res[0] = cur
            for i in range(k - 1, -1, -1):
                sub = cur[-(n - 1) : ] + str(i) if n > 1 else str(i)
                if sub not in code:
                    code.add(sub)
                    guesscode(n, k, cur + str(i), code, res)
                    break
        res = [""]
        cur = "0" * n
        code.add(cur)
        guesscode(n, k, cur, code, res)   
        return res[0]
