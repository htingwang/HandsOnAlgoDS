class Solution(object):
    def numTriplets(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                count1[nums1[i] * nums1[j]] += 1
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                count2[nums2[i] * nums2[j]] += 1
        
        res = 0
        for num in nums1:
            res += count2[num ** 2]
        for num in nums2:
            res += count1[num ** 2]
        return res
