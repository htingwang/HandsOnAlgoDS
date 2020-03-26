class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        if total_sum % 2 == 1: return False
        target = total_sum // 2
        
        bits = 1
        for num in nums:
            bits = bits | (bits << num)
        #print(bin(bits))
        #print(bin(1<<target))
        return (1 << target) & bits
