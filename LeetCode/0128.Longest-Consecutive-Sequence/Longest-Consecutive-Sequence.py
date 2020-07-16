class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nset = set(nums)
        res = 0
        for num in nums:
            if num not in nset: continue
            nset.remove(num)
            left, right = num - 1, num + 1
            while left in nset:
                nset.remove(left)
                left -= 1
            while right in nset:
                nset.remove(right)
                right += 1
            res = max(res, right - left - 1)
        return res
