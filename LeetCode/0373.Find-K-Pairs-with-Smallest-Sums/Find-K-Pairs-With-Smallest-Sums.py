class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k == 0: return []
        l1, l2 = len(nums1), len(nums2)
        idx = [0] * l1
        sz = min(l1 * l2, k)
        res = []
        for t in range(sz):
            cur = 0
            s = float('inf')
            for i in range(l1):
                #print(t, i, idx, )
                if idx[i] < l2 and nums1[i] + nums2[idx[i]] < s:
                    cur = i
                    s = nums1[cur] + nums2[idx[cur]]
            
            res.append([nums1[cur], nums2[idx[cur]]])    
            idx[cur] += 1
        return res
