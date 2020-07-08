class comp(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums_str = map(str, nums)
        nums_str.sort(key = comp)
        return "".join(nums_str) if nums_str[0] != '0' else '0'
