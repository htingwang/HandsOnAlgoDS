class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort();
        ans = 0;
        for i in range(len(nums) - 2):
            l, r = i+1, len(nums) - 1;
            while l < r:
                if nums[l] + nums[r] < target - nums[i]:
                    ans += (r - l);
                    l += 1;
                else:
                    r -= 1;
        return ans;
