class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        slist = list(s)
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                slist[i] = slist[i + 1] = '-'
                res.append("".join(slist))
                slist[i] = slist[i + 1] = '+'
        return res
