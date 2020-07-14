class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = float('inf')
        i1, i2 = -1, -1
        for i, word in enumerate(words):
            if word == word1: i1 = i
            if word == word2: i2 = i
            if i1 != -1 and i2 != -1: res = min(res, abs(i1 - i2))
        return res
