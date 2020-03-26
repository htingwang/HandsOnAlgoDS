class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        degnum = [];
        degree = {};
        degmax = 0;
        for i in range(len(nums)):
            degree[nums[i]] = degree.get(nums[i], [0,i,i]);
            degree[nums[i]][0] += 1;
            degree[nums[i]][2] = i;
            if degree[nums[i]][0] > degmax:
                degnum = [nums[i]];
            elif degree[nums[i]][0] == degmax:
                degnum.append(nums[i]);
            degmax = max(degmax, degree[nums[i]][0]);
        shortestlen = len(nums);
        for num in degnum:
            shortestlen = min(shortestlen, degree[num][2]-degree[num][1]+1);
        return shortestlen;
            
        
