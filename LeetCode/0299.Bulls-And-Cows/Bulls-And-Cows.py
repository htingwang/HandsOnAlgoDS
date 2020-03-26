class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        sh = collections.defaultdict(int)
        gh = collections.defaultdict(int)
        bull = cow = 0
        
        for x, y in zip(secret, guess):
            #print(x, y)
            if x == y:
                bull += 1
            else:
                sh[x] += 1
                gh[y] += 1
        for x in gh:
            cow += min(sh[x], gh[x])
            
        return str(bull) + "A" + str(cow) + "B"
