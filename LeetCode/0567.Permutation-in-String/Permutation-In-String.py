class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = [0] * 26
        n = len(s1)
        for i in range(n):
            count[ord(s1[i]) - ord("a")] += 1
        num = len(set(s1))
        cnt = 0
        for i in range(len(s2)): # right + n - 1 < len(s2)
            count[ord(s2[i]) - ord("a")] -= 1
            #print(count)
            if count[ord(s2[i]) - ord("a")] == 0: cnt += 1
            #print(cnt, num)
            if cnt == num: return True
            if i >= n - 1:
                count[ord(s2[i - n + 1]) - ord("a")] += 1
                if count[ord(s2[i - n + 1]) - ord("a")] == 1: cnt -= 1
        return False
