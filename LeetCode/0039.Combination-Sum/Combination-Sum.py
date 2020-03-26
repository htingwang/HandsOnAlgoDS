class Solution(object):
    def combinationSum(self, candidates, target):	
        #print [candidates, target]
        res = [];
        for i in range(len(candidates)):
            ans = [candidates[i]];
            if target == candidates[i]:
                res.append(ans);
            elif target > candidates[i]:
                subans = self.combinationSum(candidates[i:],target-candidates[i]);
                for i in subans: 
                    res.append(ans+i);
        return res;
