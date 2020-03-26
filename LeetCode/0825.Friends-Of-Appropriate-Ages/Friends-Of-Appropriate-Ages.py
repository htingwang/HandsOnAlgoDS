class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        if len(ages) < 2:
            return 0
        ages.sort()
        left = res = pre = 0
        
        for right in range(1, len(ages)):
            if ages[right] == ages[pre] and ages[right] > 14:
                res += right - pre
            while left < right and ages[left] <= 0.5 * ages[right] + 7:
                left += 1
            
            res += (right - left)
            if ages[right] != ages[pre]:
                pre = right
            #print(left, right)
        return res
