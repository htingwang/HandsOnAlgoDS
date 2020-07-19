class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        mx = 20
        mask = [1] * mx
        
        def get():
            res = 0
            for i in range(mx):
                res += (1 << i) if mask[i] > 0 else 0
            return res
        
        def update(num, sign):
            for i in range(mx):
                mask[i] += sign * (-1 if (not num & (1 << i)) else 0)
                
        res = float('inf')
        left = right = 0
        while left < len(arr) and right < len(arr):
            if left == right or cur > target:
                update(arr[right], 1)
                right += 1
            else:
                update(arr[left], -1)
                left += 1
            cur = get()
            res = min(res, abs(cur - target))
        return res
        
        
