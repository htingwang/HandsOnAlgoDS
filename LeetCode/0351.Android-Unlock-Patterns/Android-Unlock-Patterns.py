class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        jump = [[0] * 10 for _ in range(10)]
        jump[1][3] = jump[3][1] = 2
        jump[7][9] = jump[9][7] = 8
        jump[1][7] = jump[7][1] = 4
        jump[3][9] = jump[9][3] = 6
        jump[2][8] = jump[8][2] = jump[4][6] = jump[6][4] = jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5
        seen = {0}
        
        def dfs(cur, length, m, n):
            res = 0
            if m <= length <= n: res += 1
            if length > n: return 0
            seen.add(cur)
            for num in range(1, 10):
                if num not in seen and jump[cur][num] in seen:
                    res += dfs(num, length + 1, m, n)
            seen.remove(cur)
            return res
        
        
        return dfs(1, 1, m, n) * 4 + dfs(2, 1, m, n) * 4 + dfs(5, 1, m, n)
        
