class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        if len(arr) % 2 == 1: return False
        
        count = collections.defaultdict(int)
        for num in arr:
            count[num % k] += 1
        if count[0] % 2 == 1: return False
        
        for i in range(1, k // 2):
            if count[i] != count[k - i]: return False
        return True
        
