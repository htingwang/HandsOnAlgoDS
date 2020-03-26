class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for v in nums:
            if v == 0:
                nums.remove(v)
                nums.append(0)
