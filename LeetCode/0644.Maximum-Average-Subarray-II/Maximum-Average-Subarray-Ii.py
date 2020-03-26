class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = right = nums[0]
        for num in nums:
            left = min(left, num)
            right = max(right, num)
            
        while left + 1e-5 < right:
            mid = (left + right) / 2.0
            if self.check_subarray(nums, k, mid):
                left = mid
            else:
                right = mid
        return left
    
    def check_subarray(self, nums, k, average):
        s = [0] * len(nums)
        s[0] = nums[0] - average
        for i in range(len(nums) - 1):
            s[i + 1] = s[i] + nums[i + 1] - average
        #print(k, average, s)
        min_prefix = 0
        for i in range(k - 1, len(nums)):
            if s[i] - min_prefix >= 0: return True
            min_prefix = min(min_prefix, s[i - k + 1])
        return False
