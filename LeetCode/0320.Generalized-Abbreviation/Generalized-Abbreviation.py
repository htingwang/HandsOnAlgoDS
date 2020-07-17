class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        # Time: O(n * 2^n)
        return self.generateAbbreviations2(word)
    
    def generateAbbreviations2(self, word):
        res = []
        res.append("" if len(word) == 0 else str(len(word)))
        
        for i in range(len(word)):
            for a in self.generateAbbreviations2(word[i + 1 :]):
                left = str(i) if i else ""
                res.append(left + word[i] + a)
        return res
        
    def generateAbbreviations1(self, word):
        res = []
        cur = []
        def dfs(i):
            if i == len(word): 
                res.append("".join(cur))
                return
            
            cur.append(word[i])
            dfs(i + 1)
            cur.pop()
            for a in range(1, len(word) - i):
                cur.append(str(a) + word[i + a])
                dfs(i + a + 1)
                cur.pop()
            cur.append(str(len(word) - i))
            dfs(len(word))
            cur.pop()
            
        dfs(0)
        return res
