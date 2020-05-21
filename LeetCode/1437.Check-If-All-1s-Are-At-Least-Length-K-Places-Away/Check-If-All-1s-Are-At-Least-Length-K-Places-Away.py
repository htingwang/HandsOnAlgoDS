class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        pre = -1
        for i in range(n):
            if nums[i] == 1:
                #print(pre, i)
                if pre != -1 and i - pre - 1 < k: return False
                pre = i
        return True

