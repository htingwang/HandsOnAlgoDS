class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        n = len(arr)
        if n <= 1: return []
        diff = [0] * (n - 1)
        
        for i in range(n - 1):
            diff[i] = arr[i + 1] - arr[i]
            
        min_diff = min(diff)
        
        res = []
        
        for i in range(n - 1):
            if diff[i] == min_diff:
                res.append([arr[i], arr[i + 1]])
        
        return res
        
