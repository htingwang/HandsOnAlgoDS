import random
class Solution:

    def __init__(self, nums: List[int]):
        self.orig_nums = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.orig_nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        tmp_nums = self.orig_nums[:]
        for i in range(len(tmp_nums)):
            swap_idx = random.randrange(0, len(tmp_nums))
            tmp_nums[i], tmp_nums[swap_idx] = tmp_nums[swap_idx], tmp_nums[i]
        return tmp_nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
