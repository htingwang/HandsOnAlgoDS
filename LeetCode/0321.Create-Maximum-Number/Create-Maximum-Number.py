class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Time: O((m + n)^3)
        def maxArray(nums, k):
            res = []
            drop = len(nums) - k
            for num in nums:
                while res and drop and res[-1] < num:
                    res.pop()
                    drop -= 1
                res.append(num)
            return res[: k]
        
        def merge(nums1, nums2):
            i = j = 0
            res = []
            for k in range(len(nums1) + len(nums2)):
                if nums1[i :] > nums2[j :]:
                    res.append(nums1[i])
                    i += 1
                else:
                    res.append(nums2[j])
                    j += 1
            return res       
        
        res = [0] * k
        for i in range(k + 1):
            if 0 <= i <= len(nums1) and 0 <= k - i <= len(nums2):
                cur = merge(maxArray(nums1, i), maxArray(nums2, k - i))
                if  cur > res:
                    res = cur
        return res
