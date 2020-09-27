class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.res = 1
        seen = set()
        
        def dfs(s, i):
            if i == len(s):
                self.res = max(self.res, len(seen))
                #print(seen)
                return
            for j in range(i, len(s)):
                if s[i : j + 1] not in seen:
                    seen.add(s[i : j + 1])
                   # print(i, j, s[i:j+1])
                    dfs(s, j + 1)
                    seen.remove(s[i : j + 1])
        dfs(s, 0)
        return self.res
        
