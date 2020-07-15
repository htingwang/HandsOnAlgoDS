class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        count = collections.Counter(s)
        odd = None
        for c in count:
            if count[c] % 2:
                if odd: return []
                odd = c
            count[c] /= 2
        res = []
        cur = []
        def dfs(i):
            if i == len(s) //2 :
                if odd:
                    res.append("".join(cur) + odd + "".join(cur[::-1]))
                else:
                    res.append("".join(cur + cur[::-1]))
                return
            for c in count:
                if count[c]:
                    count[c] -= 1
                    cur.append(c)
                    dfs(i + 1)
                    cur.pop()
                    count[c] += 1
        dfs(0)
        return res
        
        
