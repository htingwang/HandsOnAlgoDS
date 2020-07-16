class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m1, m2 = {}, {}
        def dfs(i, j):
            if i == len(pattern) and j == len(str): return True
            if i == len(pattern) or j == len(str): return False
            
            for e in range(j, len(str)):
                p, word = pattern[i], str[j : e + 1]
                if p in m1 and m1[p] != word: continue
                if word in m2 and m2[word] != p: continue
                if p in m1:
                    if dfs(i + 1, e + 1): return True
                else:
                    m1[p] = word
                    m2[word] = p
                    if dfs(i + 1, e + 1): return True
                    del m1[p]
                    del m2[word]

            return False
            
        return dfs(0, 0)
