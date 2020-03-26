class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                left, right = j + 1, n - 1
                find = target - nums[i] - nums[j]
                #print(i, j, left, right)
                while left < right:
                    if nums[left] + nums[right] < find:
                        left += 1
                    elif nums[left] + nums[right] > find:
                        right -= 1
                    elif nums[left] + nums[right] == find:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1
                        while left < right and nums[right + 1] == nums[right]:
                            right -= 1
        return ans
                        
                        
            
        
