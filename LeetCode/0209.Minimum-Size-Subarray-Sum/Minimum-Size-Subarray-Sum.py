class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ans = sys.maxint;
        subsum = left = 0;
        for i in range(len(nums)):
            subsum += nums[i];
            while subsum >= s:
                ans = min(ans, i - left + 1);
                subsum -= nums[left];
                left += 1;
        if ans == sys.maxint: return 0;
        return ans;
