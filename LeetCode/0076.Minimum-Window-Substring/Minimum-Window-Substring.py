class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #counter = collections.Counter(t)
        counter = [0] * 128;
        for c in t:
            counter[ord(c) - ord("a")] += 1
        left = cnt = 0
        min_len = sys.maxint
        ans = ""
        #print counter
        for i in range(len(s)):
            counter[ord(s[i]) - ord("a")] -= 1
            if counter[ord(s[i]) - ord("a")] >= 0: cnt += 1
            #print(i, cnt)
            while cnt == len(t):
                #print(i, cnt, left, counter)
                if (min_len > i - left + 1):
                    min_len = i - left + 1
                    ans = s[left: i + 1]
                    #print(ans, min_len, i - left + 1)
                #print left
                counter[ord(s[left]) - ord("a")] += 1
                if counter[ord(s[left]) - ord("a")] > 0:
                    cnt -= 1           
                left += 1
        return ans
