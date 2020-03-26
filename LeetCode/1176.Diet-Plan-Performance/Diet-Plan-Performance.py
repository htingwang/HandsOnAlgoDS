class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(calories)
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + calories[i - 1]
        res = 0
        
        for i in range(k, n + 1):
            #print(s[i] - s[i - k])
            if s[i] - s[i - k] < lower:
                res -= 1
            if s[i] - s[i - k] > upper:
                res += 1
        return res
        
