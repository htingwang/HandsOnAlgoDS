class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse = 1)
        total = sum(nums)
        res = []
        cur = 0
        for num in nums:
            res.append(num)
            cur += num
            if cur > total - cur: break
        return res
