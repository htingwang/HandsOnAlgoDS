class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        for i, num in enumerate(candidates):
            ans = [num]
            if num == target:
                res.append(ans)
            if num < target:
                subans = self.combinationSum(candidates[i:], target - num)
                for sub in subans:
                    res.append(ans + sub)
            
        return res
        
