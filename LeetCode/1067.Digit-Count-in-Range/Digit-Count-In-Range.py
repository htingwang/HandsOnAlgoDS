class Solution(object):
    def digitsCount(self, d, low, high):
        """
        :type d: int
        :type low: int
        :type high: int
        :rtype: int
        """
        def count(N):
            if N == 0: return 0
            if d == 0 and N < 10: return 0
            res = 0
            if N % 10 > d: res += 1
            if N // 10: res += str(N // 10).count(str(d)) * (N % 10)
            res += N // 10 if d else N // 10 - 1
            res += count(N // 10) * 10
            return res
        return count(high + 1) - count(low)
