class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = float('-inf')
        for i in range(n):
            for j in range(i + 1, n):
                res = max(res, (nums[i] - 1) * (nums[j] - 1))
        return res
        
