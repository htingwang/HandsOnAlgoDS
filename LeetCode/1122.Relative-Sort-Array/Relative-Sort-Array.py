class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        key = {v : i for i, v in enumerate(arr2)}
        arr1.sort(key = lambda v : key.get(v, 1000 + v))
        return arr1
