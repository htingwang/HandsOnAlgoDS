class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        presum = [0] * (n + 1)
        m = {}
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
            m[presum[i + 1]] = i + 1
            
        res = 0
        for i in range(n):
            if presum[i] + k in m:
                res = max(res, m[presum[i] + k] - i)
        return res
