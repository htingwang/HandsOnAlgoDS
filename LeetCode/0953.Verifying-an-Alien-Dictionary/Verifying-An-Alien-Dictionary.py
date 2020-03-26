class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        m = {c : i for i, c in enumerate(order)}
        words_m = [[m[c] for c in w] for w in words]
        for i in range(len(words) - 1):
            if words_m[i + 1] < words_m[i]:
                return False
        return True
