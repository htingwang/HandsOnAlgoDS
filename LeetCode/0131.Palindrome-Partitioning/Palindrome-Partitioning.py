class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        valid = [[False] * n for _ in range(n)]
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 2 or valid[i + 1][j - 1]): valid[i][j] = True

        res = []
        def dfs(i, cur, res):
            if i == len(s):
                res.append(cur[:])
                return
            
            for j in range(i, len(s)):
                if valid[i][j] == True:
                    cur.append(s[i : j + 1])
                    dfs(j + 1, cur, res)
                    cur.pop()
                    
        dfs(0, [], res)
        return res
            
