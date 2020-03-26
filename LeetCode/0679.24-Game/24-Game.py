class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return False
        if len(nums) == 1: return abs(nums[0] - 24) < 1e-6
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    nums2 = [nums[k] for k in range(len(nums)) if i != k and j != k]
                    newnums = [nums[i] - nums[j]]
                    if i < j:
                        newnums.extend([nums[i] + nums[j], nums[i] * nums[j]])
                    if nums[j] != 0:
                        newnums.append(nums[i] / float(nums[j]))
                    for num in newnums:
                        nums2.append(num)
                        if self.judgePoint24(nums2): return True
                        nums2.pop()
        return False
        
