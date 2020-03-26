class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2: return True;
        flag = 0;
        for i in range(len(nums)):
            if ((i==0 or i==len(nums)-2) and nums[i+1] < nums[i]):
                flag += 1;
            elif (i<len(nums)-2 and nums[i+1] < nums[i]):
                if nums[i+2] < nums[i] and nums[i+1] < nums[i-1]:
                    return False;
                flag += 1;
            if flag >= 2:
                return False;
        return True;
        
