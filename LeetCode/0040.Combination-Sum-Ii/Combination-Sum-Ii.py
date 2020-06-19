class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.dfs(candidates, target)
        
    def dfs(self, candidates, target):
        res = []
        
        for i, num in enumerate(candidates):
            if i > 0 and num == candidates[i - 1]: continue
            ans = [num]
            if num == target:
                res.append(ans)
            if num < target:
                subans = self.combinationSum2(candidates[i + 1 : ], target - num)
                for sub in subans:
                    res.append(ans + sub)
        
        return res
