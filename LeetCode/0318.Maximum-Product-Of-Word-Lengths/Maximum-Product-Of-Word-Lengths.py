class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        n = len(words)
        encodes = [0] * n
        for i, word in enumerate(words):
            for c in word:
                encodes[i] |= (1 << (ord(c) - ord('a'))) 
        
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if encodes[i] & encodes[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res
