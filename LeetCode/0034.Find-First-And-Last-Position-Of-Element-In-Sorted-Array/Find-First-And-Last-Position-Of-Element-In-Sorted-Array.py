class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target < nums[0] or target > nums[-1]: return [-1,-1];
        lo, hi = 0, len(nums)-1;
        while lo < hi:
            mid = (lo + hi) / 2;
            if nums[mid] < target and nums[mid+1] <= target:
                lo = mid + 1;
            else:
                hi = mid;
        #print lo, hi
        if nums[lo] != target: return [-1, -1];
        ans = [lo];
        #print ans
        hi = len(nums)-1;
        while lo < hi:
            mid = (lo + hi) / 2;
            if nums[mid] <= target and nums[mid+1] <= target:
                lo = mid + 1; 
            else:
                hi = mid;
        #print lo, hi
        ans.append(lo)
        return ans;
        
