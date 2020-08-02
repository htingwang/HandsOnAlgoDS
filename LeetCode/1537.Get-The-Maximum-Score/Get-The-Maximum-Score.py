class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        #q1 = collecitons.deque(nums1)
        #q2 = collecitons.deque(nums2)
        idx1 = {num: i for i, num in enumerate(nums1)}
        idx2 = {num: i for i, num in enumerate(nums2)}
        l = max(len(nums1), len(nums2))
        memo = [[-1] * 2 for _ in range(l)]
        def dfs(i, k):
            if (k == 0 and i == len(nums1)) or (k == 1 and i == len(nums2)): return 0
            if memo[i][k] != -1: return memo[i][k]
            
            if k == 0:
                res = nums1[i] + dfs(i + 1, k)
                if nums1[i] in idx2:
                    res = max(res, nums1[i] + dfs(idx2[nums1[i]] + 1, 1))
            else:
                res = nums2[i] + dfs(i + 1, k)
                if nums2[i] in idx1:
                    res = max(res, nums2[i] + dfs(idx1[nums2[i]] + 1, 0))
            memo[i][k] = res
            return res
            
        return max(dfs(0, 0), dfs(0, 1)) % (10 ** 9 + 7)
