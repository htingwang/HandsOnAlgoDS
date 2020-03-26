class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        flag = 0;
        leftmin, rightmax = sys.maxsize, -sys.maxsize-1;
        for i in range(1, len(nums)):
            if (nums[i] < nums[i-1]):
                flag = 1;
            if (flag == 1):
                leftmin = min(leftmin, nums[i]);
        if flag == 0: return 0;
        flag = 0;
        for i in range(len(nums)-2, -1, -1):
            if (nums[i] > nums[i+1]):
                flag = 1;
            if (flag == 1):
                rightmax = max(rightmax, nums[i]);
        for left in range(len(nums)):
            if leftmin < nums[left]: break;
        for right in range(len(nums)-1, -1, -1):
            if rightmax > nums[right]: break;

        return right-left+1;
