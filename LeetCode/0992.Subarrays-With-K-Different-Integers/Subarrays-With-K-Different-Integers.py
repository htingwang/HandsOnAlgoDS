class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        left1 = left2 = cnt1 = cnt2 = ans = 0
        count1 = collections.defaultdict(int)
        count2 = collections.defaultdict(int)
        for j in range(len(A)):
            count1[A[j]] += 1
            if count1[A[j]] == 1: cnt1 += 1
            count2[A[j]] += 1
            if count2[A[j]] == 1: cnt2 += 1
            
            while cnt1 > K:
                #print j, left1, cnt1, count1
                count1[A[left1]] -= 1
                if count1[A[left1]] == 0: cnt1 -= 1
                left1 += 1
            while cnt2 >= K:
                count2[A[left2]] -= 1
                if count2[A[left2]] == 0: cnt2 -= 1
                left2 += 1
            ans += left2 - left1
        return ans
        
