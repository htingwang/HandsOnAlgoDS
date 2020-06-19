class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.dfs(range(1, 10), k, n)
    
    def dfs(self, nums, k, n): 
        res = []
        for i, num in enumerate(nums):
            ans = [num]
            if num == n and k == 1:
                res.append(ans)
            if num < n:
                subans = self.dfs(nums[i + 1: ], k - 1, n - num)
                for sub in subans:
                    res.append(ans + sub)
        return res
        
