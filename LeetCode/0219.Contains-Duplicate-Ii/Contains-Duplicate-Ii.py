class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        winset = set([]);
        for i in range(len(nums)):
            if (i > k): winset.remove(nums[i-k-1]);
            if (nums[i] in winset): return True;
            winset.add(nums[i]);
        return False;
        
