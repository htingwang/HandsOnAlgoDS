class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        missing = [0] * n
        for i in range(1, n):
            missing[i] = nums[i] - nums[i - 1] - 1 + missing[i - 1]
        if k > missing[-1]:
            return nums[-1] + k - missing[-1]
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if missing[mid] < k:
                left = mid + 1
            else:
                right = mid
        return nums[left - 1] + k - missing[left - 1]

        
