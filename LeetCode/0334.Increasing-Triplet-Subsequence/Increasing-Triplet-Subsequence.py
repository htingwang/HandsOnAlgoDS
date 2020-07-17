class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mn1 = mn2 = float('inf')
        for num in nums:
            if mn1 >= num: mn1 = num
            elif mn2 >= num: mn2 = num
            elif num > mn2: return True
        return False
        
