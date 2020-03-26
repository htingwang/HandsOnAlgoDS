class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        memo = [[0] * (n + 1) for _ in range(m + 1)]
        return self.dfs(word1, 0, word2, 0, memo)
        
    def dfs(self, word1, i, word2, j, memo):
        if i == len(word1): return len(word2) - j
        if j == len(word2): return len(word1) - i
        if memo[i][j] > 0: return memo[i][j]
        if word1[i] == word2[j]:
            return self.dfs(word1, i + 1, word2, j + 1, memo)
        else:
            insert = self.dfs(word1, i, word2, j + 1, memo)
            delete = self.dfs(word1, i + 1, word2, j, memo)
            replace = self.dfs(word1, i + 1, word2, j + 1, memo)
            memo[i][j] = min(insert, delete, replace) + 1
            return memo[i][j]
