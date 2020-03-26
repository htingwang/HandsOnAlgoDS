class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums);
        numsset = set(nums);
        return [i for i in range(1, l+1) if i not in numsset]  

