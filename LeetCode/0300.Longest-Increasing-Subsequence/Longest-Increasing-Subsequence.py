class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        min_last = [nums[0]]
        for i in range(1, n):
            if nums[i] < min_last[0]: min_last[0] = nums[i]
            elif nums[i] > min_last[-1]: min_last.append(nums[i])
            else:
                left, right = 0, len(min_last) - 1
                while left < right:
                    mid = (left + right) // 2
                    if min_last[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                min_last[left] = nums[i]
        return len(min_last)
