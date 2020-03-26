class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        num_1 = int(n)
        l = len(n)
        candidate_1 = list(n)
        for i in range(l // 2):
            candidate_1[l - 1 - i] = candidate_1[i]
            
        diff_1 = (abs(num_1 - int("".join(candidate_1))), int("".join(candidate_1)))
        
        #1000
        # 911
        num_2 = num_1 - 10 ** (l - 1 - (l - 1) // 2)
        #print(num_2)
        candidate_2 = list(str(num_2))
        if len(candidate_2) < l:
            candidate_2[(len(candidate_2) - 1) // 2] = "9"
        for i in range(len(candidate_2) // 2):
            candidate_2[len(candidate_2) - 1 - i] = candidate_2[i]
        diff_2 = (abs(num_1 - int("".join(candidate_2))), int("".join(candidate_2)))
        
        num_3 = num_1 + 10 ** (l - 1 - (l - 1) // 2)
        candidate_3 = list(str(num_3))
        for i in range(len(candidate_3) // 2):
            candidate_3[len(candidate_3) - 1 - i] = candidate_3[i]
        diff_3 = (abs(num_1 - int("".join(candidate_3))),int("".join(candidate_3)))
        
        result = sorted([diff_1, diff_2, diff_3])
        #print(result)
        return str(result[0][1]) if result[0][0] != 0 else str(result[1][1])
