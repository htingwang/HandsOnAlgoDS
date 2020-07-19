class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.lengthOfLIS2(nums)
    
    def lengthOfLIS2(self, nums):
        dp = []
        for num in nums:
            i = bisect.bisect_left(dp, num)
            if i == len(dp): dp.append(num)
            else: dp[i] = num
        return len(dp)
    
    def lengthOfLIS1(self, nums):
        if not nums: return 0
        n = len(nums)
        min_last = [nums[0]]
        for i in range(1, n):
            if nums[i] < min_last[0]: min_last[0] = nums[i]
            elif nums[i] > min_last[-1]: min_last.append(nums[i])
            else:
                left, right = 0, len(min_last) - 1
                while left < right:
                    mid = (left + right) // 2
                    if min_last[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                min_last[left] = nums[i]
        return len(min_last)
        
