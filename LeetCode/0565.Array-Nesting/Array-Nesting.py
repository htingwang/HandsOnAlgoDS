class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        exists = set();
        maxlen = 0;
        for i in range(len(nums)):
            count = 0;
            idx = i;
            while True:
                if idx in exists:    
                    maxlen = max(maxlen, count);
                    if i == idx: break;
                exists.add(idx);
                idx = nums[idx];
                count += 1;
        return maxlen;
            
