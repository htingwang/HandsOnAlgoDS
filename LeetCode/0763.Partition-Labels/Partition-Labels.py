from collections import Counter
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S: return []
        count = Counter(S)
        res = []
        sub_len = rest_num = 0
        sub_count = {}
        for i, c in enumerate(S):
            if c not in sub_count:
                sub_count[c] = count[c] - 1
                rest_num += sub_count[c]
            else:
                sub_count[c] -= 1
                rest_num -= 1
            sub_len += 1
            if rest_num == 0:
                res.append(sub_len)
                sub_len = 0
        return res
