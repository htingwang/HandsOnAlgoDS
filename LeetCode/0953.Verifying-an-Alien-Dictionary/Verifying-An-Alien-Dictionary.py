class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        return self.isAlienSorted2(words, order)

    def isAlienSorted1(self, words, order):
        m = {c : i for i, c in enumerate(order)}
        words_m = [[m[c] for c in w] for w in words]
        for i in range(len(words) - 1):
            if words_m[i + 1] < words_m[i]:
                return False
        return True

    def isAlienSorted2(self, words, order):
        idx = {c: i for i, c in enumerate(order)}
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            j = 0
            while j < min(len(w1), len(w2)):
                if idx[w2[j]] > idx[w1[j]]: break
                if idx[w2[j]] < idx[w1[j]]: 
                    return False
                j += 1
            if j == min(len(w1), len(w2)) and len(w2) < len(w1): return False
        return True