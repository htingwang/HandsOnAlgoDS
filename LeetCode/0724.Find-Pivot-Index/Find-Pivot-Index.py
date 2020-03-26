class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums);
        subsum = 0;
        for i in range(len(nums)):
            if (subsum*2+nums[i] == total): return i;
            subsum += nums[i]
        return -1;
