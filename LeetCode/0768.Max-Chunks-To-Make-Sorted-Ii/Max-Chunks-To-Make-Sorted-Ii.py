class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 1
        n = len(arr)
        b = list(arr)
        for i in range(n - 2, -1, -1):
            b[i] = min(b[i + 1], b[i])
        #print(b)
        cur_max = float('-inf')
        for i in range(n - 1):
            cur_max = max(cur_max, arr[i])
            if cur_max <= b[i + 1]:
                res += 1
        return res
