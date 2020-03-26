class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = curEnd = curFarthest = 0;
        for i in range(len(nums)-1):
            curFarthest = max(curFarthest, i + nums[i]);
            if (i == curEnd) :
                jumps += 1;
                curEnd = curFarthest;   
        return jumps;
        
