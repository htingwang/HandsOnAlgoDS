class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0] * (num + 1)
        power = 1
        for i in range(1, num + 1):
            if i == power * 2: power *= 2
            res[i] = 1 + res[i - power]
        return res
