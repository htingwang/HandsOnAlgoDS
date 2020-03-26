class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str2) > len(str1):
            str1, str2 = str2, str1;
        ans = "";
        len1, len2 = len(str1), len(str2);
        if str2 not in str1: return "";
        rlist, i, n = [], 1, len2;
        #print n
        while i <= n:
            if n % i == 0:
                rlist.append(i);
            i += 1;
        #print rlist
        for i in rlist:
            #print i, str2[:len2/i-1] * i
            if str2 == str2[:len2/i] * i and str1 == str2[:len2/i] * (len1 / (len2/i)):
                ans = str2[:len2/i];
                break;
        #print ans
        return ans;
