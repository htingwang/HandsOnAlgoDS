class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        memo = {}
        
        def dfs(s):
            if s in memo: return memo[s]
            res = []
            for i, c in enumerate(s):
                if c in {'+', '-', '*'}:
                    left = dfs(s[: i])
                    right = dfs(s[i + 1 :])
                    for a in left:
                        for b in right:
                            if c == '+': res.append(a + b)
                            if c == '-': res.append(a - b)
                            if c == '*': res.append(a * b)
            if not res: return [int(s)]
            memo[s] = res
            return res
        return dfs(input)
