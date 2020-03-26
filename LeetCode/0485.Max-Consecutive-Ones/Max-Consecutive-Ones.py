class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, cnt = 0, 0;
        for num in nums:
            if (num == 1):
                cnt += 1;
            else:
                cnt = 0;
            result = max(result, cnt);
        
        return result;
            
        
