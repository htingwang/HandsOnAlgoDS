class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2: return len(nums)
        pre, cur, cnt = 0, 1, 0
        while cur < len(nums):
            if nums[cur] == nums[pre]:
                if cnt < 1:
                    pre += 1
                    nums[pre] = nums[cur]
                cnt += 1
            else:
                pre += 1
                nums[pre] = nums[cur]
                cnt = 0
            cur += 1
        return pre + 1
