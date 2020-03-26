class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2, = len(nums1), len(nums2);
        l = l1 + l2;
        i1 = i2 = i = 0;
        midpos = l/2;
        while i1 < l1 or i2 < l2:
            if i2 >= l2 or (i1 < l1 and nums1[i1] < nums2[i2]):
                val = nums1[i1];
                i1 += 1;
            else:
                val = nums2[i2];
                i2 += 1;
            if i == midpos:
                mid1 = val;
                break;
            if i == midpos-1:
                mid2 = val;
            i += 1;
        if l%2 == 1:
            return mid1;
        else:
            return float((mid1+mid2))/2;
