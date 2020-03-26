from collections import Counter
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = ""
        count = Counter(T)
        for c in S:
            if c in count:
                res += c *  count[c]
                del count[c]
        for c in count:
            res += c *  count[c]
        return res
