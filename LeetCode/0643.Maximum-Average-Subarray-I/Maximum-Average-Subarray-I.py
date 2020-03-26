class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        submax = sub = sum(nums[0:k]);
        for i in range(k, len(nums)):
            sub = sub+nums[i]-nums[i-k];
            submax = max(submax, sub);
        return float(submax)/k;
