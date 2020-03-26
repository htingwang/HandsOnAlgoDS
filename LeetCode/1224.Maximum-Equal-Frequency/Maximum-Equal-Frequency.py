class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        occurence = collections.defaultdict(int)
        count = collections.defaultdict(int)
        for i, num in enumerate(nums):
            count[num] += 1
            occurence[count[num]] += 1
            occurence[count[num] - 1] -= 1
            if occurence[count[num] - 1] <= 0:
                del occurence[count[num] - 1]
            #print(i, occurence)
            occur_list = occurence.items()
            if len(occurence) == 2:
                #print(occur_list)
                if occur_list[0] == (1, 1) or occur_list[1] == (1, 1):
                    res = max(res, i + 1)
                if abs(occur_list[0][0] - occur_list[1][0]) == 1:
                    if occur_list[0][0] > occur_list[1][0] and occur_list[0][1] == 1:
                        res = max(res, i + 1)
                    if occur_list[0][0] < occur_list[1][0] and occur_list[1][1] == 1:
                        res = max(res, i + 1)
            if len(occurence) == 1 and (occur_list[0][0] == 1 or occur_list[0][1] == 1):
                res = max(res, i + 1)
        return res
            
        
