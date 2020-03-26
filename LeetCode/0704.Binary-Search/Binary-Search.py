class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1;
        l, r = 0, len(nums) - 1;
        while l < r:
            mid = (l + r) / 2;
            if nums[mid] < target:
                l = mid + 1;
            else:
                r = mid;
        if nums[l] == target: return l;
        else: return -1;
        
