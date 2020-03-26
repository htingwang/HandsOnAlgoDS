class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # left <= target < right
        left, right = 0, len(nums);
        while left < right:
            middle = (left+right)/2;
            if nums[middle] < target:
                left = middle+1;
            else:
                right = middle;
        return left;
            
