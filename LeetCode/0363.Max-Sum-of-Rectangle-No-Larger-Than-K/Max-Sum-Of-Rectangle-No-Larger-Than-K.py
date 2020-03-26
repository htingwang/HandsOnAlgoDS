class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        res = float('-inf')
        m, n = len(matrix), len(matrix[0])
        for l in range(n):
            sums = [0] * m
            for r in range(l, n):
                for i in range(m):
                    sums[i] += matrix[i][r]
                res = max(res, self.maxSumSubArray(sums, k))
        return res
    
    def maxSumSubArray(self, array, k):
        pre = [0]
        cur, res = 0, float('-inf')
        for num in array:
            cur += num
            best = bisect.bisect_left(pre, cur - k)
            if best != len(pre): res = max(res, cur - pre[best])
            bisect.insort(pre, cur)
        return res
