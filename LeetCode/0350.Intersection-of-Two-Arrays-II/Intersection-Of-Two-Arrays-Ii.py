class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        
        res = []
        for key in count2:
            if key in count1:
                res.extend([key] * min(count1[key], count2[key]))
        return res
