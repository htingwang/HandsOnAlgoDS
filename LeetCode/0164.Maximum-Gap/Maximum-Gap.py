class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.maximumGap2(nums)
        
    def maximumGap2(self, nums):
        n = len(nums)
        if n < 2: return 0
        
        mx = max(nums)
        exp, radix = 1, 10
        aux = [0] * n
        
        while mx // exp:
            count = [0] * radix
            for i in range(n):
                count[(nums[i] // exp) % radix] += 1

            for i in range(1, radix):
                count[i] += count[i - 1]

            for i in range(n - 1, -1, -1):
                count[(nums[i] // exp) % radix] -= 1
                aux[count[(nums[i] // exp) % radix]] = nums[i]

            for i in range(n):
                nums[i] = aux[i]
            exp *= 10
        
        res = 0
        for i in range(1, n):
            res = max(res, nums[i] - nums[i - 1])
        
        return res
        
        
    def maximumGap1(self, nums):
        n = len(nums)
        if n < 2: return 0
        mx, mn = max(nums), min(nums)
        size = (mx - mn) // n + 1
        cnt = (mx - mn) // size + 1
        bucket_max = [float('-inf')] * cnt
        bucket_min = [float('inf')] * cnt
        for num in nums:
            idx = (num - mn) // size
            bucket_max[idx] = max(bucket_max[idx], num)
            bucket_min[idx] = min(bucket_min[idx], num)
            
        res, pre = 0, 0
        for i in range(1, cnt):
            if bucket_min[i] == float('inf') or bucket_max[i] == float('-inf'): continue
            res = max(res, bucket_min[i] - bucket_max[pre])
            pre = i
        #print(bucket_min, bucket_max)
        return res
            
        
