class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        dp = [[0, -1] for _ in range(n)]
        nums.sort()
        mx_len = mx_idx = -1
        for i, num in enumerate(nums):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = j
            mx_len = max(mx_len, dp[i][0])
            if dp[i][0] == mx_len: mx_idx = i
        #print(dp)
        res = collections.deque()
        while mx_idx != -1:
            res.appendleft(nums[mx_idx])
            mx_idx = dp[mx_idx][1]
        return list(res)
