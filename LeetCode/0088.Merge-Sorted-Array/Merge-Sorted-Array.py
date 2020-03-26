class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m-1, n-1, m+n-1;
        while j >= 0:
            if i<0 or nums2[j] >= nums1[i]:
                nums1[k] = nums2[j];
                j -= 1;
            else:
                nums1[k] = nums1[i];
                i -= 1;
            k -= 1;
        
                
        
        
