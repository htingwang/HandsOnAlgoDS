class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = right = cnt = res = 0
        n = len(nums)
        while left < n and right < n:
            if nums[right] % 2 == 1:
                cnt += 1
            if cnt == k:
                pre_left = left
                while left <= right and nums[left] % 2 == 0:
                    left += 1
                pre_right = right
                while right + 1 < n and nums[right + 1] % 2 == 0:
                    right += 1
                res += (left - pre_left + 1) * (right - pre_right + 1)
                left += 1
                cnt -= 1
            right += 1
        return res
