class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.m = collections.defaultdict(list)
        for i, word in enumerate(words):
            self.m[word].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1, idx2 = self.m[word1], self.m[word2]
        res = float('inf')
        i = j = 0
        while i < len(idx1) and j < len(idx2):
            res = min(res, abs(idx1[i] - idx2[j]))
            if idx1[i] < idx2[j]: i += 1
            else: j += 1
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
