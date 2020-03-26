class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = max(nums);
        targetIdx = nums.index(target);
        for num in nums:
            if num != target and num*2 > target: return -1;
            
        return targetIdx;
