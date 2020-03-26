class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return None;
        n = len(nums);
        if nums[0] <= nums[n - 1]: return nums[0];
        start, end = 1, n - 1;
        while start < end:
            mid = (start + end) // 2;
            if nums[mid] > nums[n - 1]:
                start = mid + 1;
            else:
                end = mid;
        return nums[start]
