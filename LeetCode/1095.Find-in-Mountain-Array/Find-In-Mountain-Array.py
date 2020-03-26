# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        n = mountain_arr.length()
        left, right = 0, n-1

    
        while left < right:
            mid = (left + right) / 2
            if (mountain_arr.get(mid) > mountain_arr.get(mid + 1)):
                right = mid
            else:
                left = mid + 1
        peak = mountain_arr.get(left)
        peak = left
        #print peak
        left, right = 0, peak
        while left < right:
            #print left, right, mid
            mid = (left + right) / 2
            if target > mountain_arr.get(mid):
                left = mid + 1
            else:
                right = mid
        if mountain_arr.get(left) == target: return left
        #print left
        left, right = peak + 1, n - 1
        while left < right:
            mid = (left + right) / 2
            #print left, right, mid, n
            if target < mountain_arr.get(mid):
                left = mid + 1
            else:
                right = mid
        if mountain_arr.get(left) == target: return left
        return -1
            
