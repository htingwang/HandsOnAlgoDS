class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = float('inf')
        i1 = i2 = -1
        for i, word in enumerate(words):
            tmp = i1
            if word == word1: i1 = i
            if word == word2: i2 = i
            if i1 == i2 and tmp != -1 and tmp != i1: 
                res = min(res, i1 - tmp)
            elif i1 != i2 and i1 != -1 and i2 != -1:
                res = min(res, abs(i1 - i2))
        return res
            
