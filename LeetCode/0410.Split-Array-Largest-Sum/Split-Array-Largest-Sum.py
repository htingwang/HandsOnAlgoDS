class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.check(nums, mid) <= m:
                right = mid
            else:
                left = mid + 1
        return right
    
    def check(self, nums, val):
        res = 1
        cur = 0
        for num in nums:
            cur += num
            if cur > val:
                res += 1
                cur = num
        return res
