class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort();
        ans = sum(nums[:3]);
        mindiff = abs(target-ans);
        for i in range(len(nums)-2):
            if target < sum(nums[i:i+3]) and abs(target-sum(nums[i:i+3])) > abs(mindiff):
                return ans;
            l, r = i+1, len(nums)-1;
            while l < r:
                tmpsum = nums[i]+nums[l]+nums[r];
                if abs(target-tmpsum) < mindiff:
                    ans = tmpsum;
                    mindiff = abs(target-tmpsum);
                if tmpsum == target: return target;
                elif tmpsum < target: l+=1;
                else: r-=1;
        return ans;
