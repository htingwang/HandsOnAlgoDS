class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        # Time: O(n * 2^n)
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
