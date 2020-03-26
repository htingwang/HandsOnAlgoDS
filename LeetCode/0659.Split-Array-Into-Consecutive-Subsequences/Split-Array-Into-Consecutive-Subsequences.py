class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        headlist = []
        taillist = []
        count = collections.Counter(nums)
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]: continue
            if count[num] - count[num - 1] > 0:
                #head += count[num] - count[num - 1]
                headlist += [num] * (count[num] - count[num - 1])
            if count[num] - count[num + 1] > 0:
                #tail += count[num] - count[num + 1]
                taillist += [num] * (count[num] - count[num + 1])
        #print(headlist)
        #print(taillist)
        if len(headlist) != len(taillist): return False
        for i in range(len(headlist)):
            if taillist[i] - headlist[i] < 2: return False
        return True
        
