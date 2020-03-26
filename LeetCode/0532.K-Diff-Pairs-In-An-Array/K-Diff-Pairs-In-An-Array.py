class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        exists = {};
        count = 0;
        if k < 0: return 0;
        for i in range(len(nums)):
            exists[nums[i]] = exists.get(nums[i], 0) + 1;
        for num in exists:
            if k == 0:
                if exists[num] >= 2: count += 1;
            else:
                if exists.get(num+k, 0) >= 1: count += 1;
                #if exists.get(num-k, 0) >= 1: count += 1;
            #exists[num] = 0;
        return count;
                
        
