class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, cur = 0, 0;
        for i in range(len(nums)):
            if (i and nums[i-1] >= nums[i]):
                cur = i;
            ans = max(ans, i-cur+1)
        return ans;
