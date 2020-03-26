class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums);
        if nums[0] < nums[n - 1]: return nums[0];
        start, end = 0, n - 1;
        while start < end:
            mid = (start + end) // 2;
            #print start, end, mid
            if start == mid: return min(nums[start], nums[end])
            if nums[mid] > nums[end]:
                start = mid + 1;
            elif nums[mid] < nums[start]:
                end = mid;
            else:
                end -= 1;
            #print start, end
        return nums[start]
        
