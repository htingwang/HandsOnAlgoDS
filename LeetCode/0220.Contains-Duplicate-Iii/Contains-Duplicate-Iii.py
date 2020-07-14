class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        d = {}
        for i, num in enumerate(nums):
            b = num // t if t != 0 else num
            for key in (b - 1, b, b + 1):
                if key in d and abs(d[key] - num) <= t: return True
            d[b] = num
            if i >= k: del[d[nums[i - k] // t if t != 0 else d[nums[i - k]]]]
        return False
        
