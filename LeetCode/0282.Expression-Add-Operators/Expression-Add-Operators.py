class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def dfs(idx, tmp, tot, last, res):
            if idx == len(num):
                if tot == target:
                    res.append(tmp)
                return
            for i in range(idx, len(num)):
                x = int(num[idx: i + 1])
                if idx == 0:
                    dfs(i + 1, str(x), x, x, res)
                else:
                    dfs(i + 1, tmp + "+" + str(x), tot + x, x, res)
                    dfs(i + 1, tmp + "-" + str(x), tot - x, -x, res)
                    dfs(i + 1, tmp + "*" + str(x), tot - last + last * x, last * x, res)
                if x == 0:
                    break
        res = []
        dfs(0, "", 0, 0, res)
        return res        
