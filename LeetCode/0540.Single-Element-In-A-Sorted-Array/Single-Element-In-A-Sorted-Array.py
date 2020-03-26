class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            #print(left, right , mid)
            if (mid == 0 or nums[mid - 1] != nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] != nums[mid]):
                return nums[mid]
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                left = mid + 1
            else:
                right = mid - 1
        return -1
