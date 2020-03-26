class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        balloon = collections.Counter("balloon")
        count = 0
        res = 0
        text_count = collections.Counter(text)
        return min(text_count["b"], text_count["a"],text_count["l"] // 2, text_count["o"] // 2, text_count["n"])        
