class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        p = q = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                p = q + 1
            if nums[i] < nums[i - 1]:
                q = p + 1
            #print(i, p, q)
    
        return max(p, q)

