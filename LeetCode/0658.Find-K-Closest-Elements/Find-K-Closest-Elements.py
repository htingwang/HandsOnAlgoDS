class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if len(arr) == 1: return arr
        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
        left = max(0, left - k - 1)
        right = min(len(arr) - 1, right + k - 1)
        #print(left, right)
        while right - left > k - 1:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
            #print(left, right)
        return arr[left :  right + 1]
