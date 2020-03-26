class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 1
        for k in range(2, int(math.sqrt(N * 2)) + 1):
            if (N - (k * (k - 1) / 2)) % k == 0:
                count += 1
        return count
