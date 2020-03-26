class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1;
        #if len(nums) > 0 and nums[0] == target: return 0;
        l, r = 0, len(nums)-1;
        while l + 1 < r:
            mid = (l + r) / 2;
            #print [l, r, mid, nums[mid], target]
            if nums[mid] == target:
                return mid;
            if (nums[mid] < target <= nums[r]) or (target <= nums[r] < nums[mid]) or (nums[r] <= nums[mid] < target):
                l = mid;
            else:
                r = mid;
        #print l
        if nums[l] == target: return l;
        if nums[r] == target: return r;
        return -1;
