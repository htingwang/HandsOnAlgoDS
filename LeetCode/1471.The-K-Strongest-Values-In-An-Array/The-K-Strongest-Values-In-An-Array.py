class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        n = len(arr)
        l, r = 0, n - 1
        res = []
        m = arr[(n - 1) // 2]
        while k > 0:
            if arr[r] - m < m - arr[l]:
                res.append(arr[l])
                l += 1
            else:
                res.append(arr[r])
                r -= 1
            k -= 1
        return res
        
